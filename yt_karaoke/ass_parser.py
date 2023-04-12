import numpy as np

template = """[Script Info]
ScriptType: v4.00+
PlayResX: 384
PlayResY: 288
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def secs_to_hhmmss(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return f"{hh:0>1.0f}:{mm:0>2.0f}:{ss:0>2.2f}"

# See http://www.tcax.org/docs/ass-specs.htm
# and this tutorial on Aegisub https://www.youtube.com/watch?v=pfrABpkNWsE
def generate_dialogue(transcript):
    lines = []
    for segment in transcript["segments"]:
        chars = []
        for cidx, crow in segment["char-segments"].iterrows():
            if (
                np.isnan(crow["start"]) and crow["char"] == " "
            ):  # usually the first row is empty
                continue

            if np.isnan(crow["start"]):
                length = "0"
            else:
                length = str(round(((crow["end"]) - crow["start"]) * 100))
            chars.append("{\\k" + length + "}" + crow["char"])

        line = f"Dialogue: 0,{secs_to_hhmmss(segment['start'])},{secs_to_hhmmss(segment['end'])},Default,,0,0,0,,{''.join(chars)}"
        lines.append(line)
    return "\n".join(lines)


def write_ass_file(transcript, path):
    with open(path, "w") as f:
        f.write(f"{template}\n{generate_dialogue(transcript)}")
