import argparse
import os
import subprocess
import sys
import tempfile
import wave

import torch
import whisper
import whisperx
import yt_dlp
from ass_parser import write_ass_file


def check_err(result):
    if result.returncode != 0:
        print(result.stderr)
        return sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "yt_video_url",
        type=str,
        help="the youtube video url to process (eg 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')",
    )
    parser.add_argument(
        "--model",
        default="base",
        choices=whisper.available_models(),
        help="name of the Whisper model to use",
    )
    parser.add_argument(
        "--align_model",
        default="WAV2VEC2_ASR_BASE_960H",
        help="name of phoneme-level ASR model to use with Whisperx",
    )
    parser.add_argument(
        "--device",
        default="cuda" if torch.cuda.is_available() else "cpu",
        help="device to use for PyTorch inference",
    )
    parser.add_argument(
        "--shifts",
        default=1,
        type=int,
        help="Number of random shifts for equivariant stabilization in Demucs.",
    )

    args = parser.parse_args().__dict__
    temp_dir = tempfile.gettempdir()
    device = args.pop("device")
    whisper_model = args.pop("model")
    alignment_model = args.pop("align_model")
    yt_url = args.pop("yt_video_url")
    yt_id = yt_url.split("v=")[-1]
    demucs_shifts = args.pop("shifts")

    # Download audio
    ydl_opts = {
        "outtmpl": os.path.join(temp_dir, "%(id)s.%(ext)s"),
        "quiet": True,
        "verbose": False,
        "format": "mp3/bestaudio/best",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])
        print(f"Downloaded {yt_url}")

    print("Separating vocals with Demucs (this may take a while)...")
    separated_path = os.path.join(temp_dir, "separated")
    mp3_path = os.path.join(temp_dir, f"{yt_id}.mp3")
    cmd = [
        "demucs",
        "--two-stems=vocals",
        f"--device={device}",
        f"--shifts={demucs_shifts}",
        f"--out={separated_path}",
        f"{mp3_path}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    check_err(result)

    print("Separated vocals, transcribing with Whisper")
    audio_file_path = f"{separated_path}/htdemucs/{yt_id}/vocals.wav"
    model = whisper.load_model(whisper_model, device)
    result = model.transcribe(audio_file_path)

    print("Transcribed, aligning with Whisperx")
    model_a, metadata = whisperx.load_align_model(
        language_code=result["language"], device=device, model_name=alignment_model
    )
    transcript = whisperx.align(
        result["segments"], model_a, metadata, audio_file_path, device
    )

    print("Building ASS file")
    subtitles_path = os.path.join(temp_dir, f"{yt_id}.ass")
    write_ass_file(transcript, subtitles_path)

    print("Building karaoke video")
    instrumental_path = f"{separated_path}/htdemucs/{yt_id}/no_vocals.wav"
    with wave.open(instrumental_path, "r") as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = round(frames / float(rate), 2)

    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "lavfi",
        "-i",
        f"color=size=1280x720:duration={duration}:rate=24:color=black",
        "-i",
        instrumental_path,
        "-vf",
        f"ass={subtitles_path}",
        "-shortest",
        "-c:v",
        "libx264",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "karaoke.mp4",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    check_err(result)

    print("karaoke.mp4 ready!")


if __name__ == "__main__":
    main()
