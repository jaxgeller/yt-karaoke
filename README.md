# YT-Karaoke

This CLI uses [Demucs](https://github.com/facebookresearch/demucs) and [Whisperx](https://github.com/m-bain/whisperX) to extract vocals from a YouTube video, transcribe the lyrics, and then generate a karaoke video.

## Installation

To get started, you'll need Python 3.9 and [ffmpeg](https://ffmpeg.org/) installed. Then, install the CLI with pip

```
pip install git+https://github.com/jaxgeller/yt-karaoke.git
```

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

You'll get your best results running this CLI with cuda on the largest whisper models, as well as good quality audio from Youtube. See this Colab notebook for a demo of the CLI running with GPU's and the largest models.

In my testing, rock songs tend to do very well while rap accuracy tends to suffer.
