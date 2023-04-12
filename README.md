# YT-Karaoke

This CLI uses [Demucs](https://github.com/facebookresearch/demucs) and [Whisperx](https://github.com/m-bain/whisperX) to extract vocals from a YouTube video, transcribe the lyrics on a per-character level, and then generate a karaoke video with real-time subtitles.

https://user-images.githubusercontent.com/4494509/231500841-37644652-3b45-481b-ae83-5c3c731ceb53.mp4

_Demo of "All Star" generated using the highest settings._

## Installation

To get started, you'll need Python 3.8+ and [ffmpeg](https://ffmpeg.org/) installed. Then, install the CLI with pip

```
pip install git+https://github.com/jaxgeller/yt-karaoke.git
```

Or you can checkout the notebook

<a target="_blank" href="https://colab.research.google.com/github/jaxgeller/yt-karaoke/blob/main/notebook.ipynb">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Usage

To use the CLI, simply run `yt_karaoke` with a YouTube URL as the first argument. This may take awhile

```
yt_karaoke "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

To run with the highest possible accuracy, use

```
yt_karaoke "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --device cuda --model large --align_model WAV2VEC2_ASR_LARGE_LV60K_960H --shifts 10
```

## Results

Using this notebook, I've generated karaoke videos for the following songs. The results are pretty good, but there's still a lot of room for improvement. If you have any suggestions, please open an issue or PR.

- All Star: Great transcription, separation, and character alignment
- Buddy Holly: Good transcription, but not great in some of the verses. Does pick up on the "Woo-hoos" in the chorus. Character alignment is solid.
- God's Plan: Not the best instrumental separation by Demucs or transcription by Whisper, but adlibs are picked up correctly.
- Parked by the Lake: Good transcription and alignment, but WhisperX might have a bug in aligning numeric characters. Lookout for when "80 miles" shows up in video.
