from pathlib import Path
import subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output'
LOGO = ROOT.parents[5] / 'workflow' / 'assets' / 'shop-branding.png'
# Project is nested six directories below repository root.
if not LOGO.exists():
    LOGO = Path('C:/Users/vuodo/software/TikTok-AI-Editor/workflow/assets/shop-branding.png')

src = Image.open(LOGO).convert('RGBA').crop((227, 0, 1027, 800)).resize((68, 68), Image.Resampling.LANCZOS)
mask = Image.new('L', (68, 68), 0)
ImageDraw.Draw(mask).ellipse((0, 0, 67, 67), fill=255)
src.putalpha(mask)
src.save(OUT / 'shop-brand-circle-68.png')

ass = '''[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Main,Arial,42,&H00FFFFFF,&H00FFFFFF,&HBE171717,&H60000000,-1,0,0,0,100,100,0,0,1,3,0,8,48,48,80,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:02.44,Main,,0,0,0,,Ủa, một giá mà treo được\\Nhai tầng luôn á?
Dialogue: 0,0:00:02.44,0:00:03.72,Main,,0,0,0,,Thanh trên, thanh dưới—
Dialogue: 0,0:00:03.76,0:00:05.20,Main,,0,0,0,,chia đồ ra là thấy ngay.
Dialogue: 0,0:00:05.64,0:00:07.20,Main,,0,0,0,,Có nhiều phân loại đó,
Dialogue: 0,0:00:07.20,0:00:08.84,Main,,0,0,0,,chọn đúng mẫu trong giỏ nha!
'''
(OUT / 'final-captions.ass').write_text(ass, encoding='utf-8')

fc = (
    '[0:v]trim=start_frame=0:end_frame=75,setpts=PTS-STARTPTS[v0];'
    '[1:v]trim=start_frame=108:end_frame=144,setpts=PTS-STARTPTS[v1];'
    '[0:v]trim=start_frame=140:end_frame=176,setpts=PTS-STARTPTS[v2];'
    '[2:v]trim=start_frame=87:end_frame=180,setpts=PTS-STARTPTS[v3];'
    '[v0][v1][v2][v3]concat=n=4:v=1:a=0[v];'
    '[v][4:v]overlay=x=566:y=1124:format=auto,format=yuv420p,ass=output/final-captions.ass[vout]'
)
cmd = ['ffmpeg', '-hide_banner', '-y',
       '-i', str(OUT / 'scene-01-flow-attempt-08.mp4'),
       '-i', str(OUT / 'scene-01-flow-attempt-03.mp4'),
       '-i', str(OUT / 'scene-01-flow-attempt-04.mp4'),
       '-i', str(OUT / 'attempt08-flow-audio.m4a'),
       '-loop', '1', '-framerate', '24', '-i', str(OUT / 'shop-brand-circle-68.png'),
       '-filter_complex', fc, '-map', '[vout]', '-map', '3:a:0',
       '-frames:v', '240', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
       '-r', '24', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
       '-t', '10.000', '-movflags', '+faststart', str(OUT / 'final_video-v2.mp4')]
subprocess.run(cmd, cwd=ROOT, check=True)
