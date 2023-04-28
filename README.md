# YT-Karaoke

This CLI uses [Demucs](https://github.com/facebookresearch/demucs) and [Whisperx](https://github.com/m-bain/whisperX) to extract vocals from a YouTube video, transcribe the lyrics on a per-character level, and then generate a karaoke video with real-time subtitles. For more details see [this blog post](https://www.jaxgeller.com/using-ai-to-turn-youtube-videos-into-karaoke/).

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

Using [this notebook](https://colab.research.google.com/github/jaxgeller/yt-karaoke/blob/main/notebook.ipynb), I've generated karaoke videos for the following songs. The results are pretty good, but there's still a lot of room for improvement. If you have any suggestions, please open an issue or PR.

- [All Star - Smash Mouth](https://user-images.githubusercontent.com/4494509/231500841-37644652-3b45-481b-ae83-5c3c731ceb53.mp4): Great transcription, separation, and character alignment
- [Buddy Holly - Weezer](https://user-images.githubusercontent.com/4494509/231512619-5dbef49e-ce65-4675-b4c2-16ea9d37b503.mp4): Good transcription, but not great in some of the verses. Does pick up on the "Woo-hoos" in the chorus. Character alignment is solid.
- [God's Plan - Drake](https://user-images.githubusercontent.com/4494509/231512741-ead38230-2a38-49da-85f0-299224bc6552.mp4): Not the best instrumental separation by Demucs or transcription by Whisper, but adlibs are picked up correctly.
- [Parked by the Lake - Dean Summerwind](https://user-images.githubusercontent.com/4494509/231512783-7bcdfac9-b3d8-4387-b245-0bd8d76d252a.mp4): Good transcription and alignment, but WhisperX might have a bug in aligning numeric characters. Lookout for when "80 miles" shows up in video.
