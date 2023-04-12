# YT-Karaoke

This CLI uses [Demucs](https://github.com/facebookresearch/demucs) and [Whisperx](https://github.com/m-bain/whisperX) to extract vocals from a YouTube video, transcribe the lyrics on a per-character level, and then generate a karaoke video with real-time subtitles. 




https://user-images.githubusercontent.com/4494509/231500841-37644652-3b45-481b-ae83-5c3c731ceb53.mp4

_Demo of "All Star" generated using the highest settings._


## Installation

To get started, you'll need Python 3.8+ and [ffmpeg](https://ffmpeg.org/) installed. Then, install the CLI with pip

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
