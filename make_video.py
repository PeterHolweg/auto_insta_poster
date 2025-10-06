import subprocess
from pathlib import Path
from typing import List




def make_slideshow(image_paths: List[Path], out_file: Path, duration_per_image: int = 2, size: str = "1080:1350") -> Path:
"""Creates an MP4 slideshow. size default is 1080x1350 (4:5) suitable for Instagram feed.
Make sure ffmpeg is on PATH.
"""
# Create a temporary file list for ffmpeg
list_file = out_file.parent / "ff_list.txt"
with open(list_file, "w") as f:
for p in image_paths:
f.write(f"file '{p.resolve()}'\n")
f.write(f"duration {duration_per_image}\n")
# repeat last image to avoid short video issues
f.write(f"file '{image_paths[-1].resolve()}'\n")


cmd = [
"ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file),
"-vf", f"scale={size},format=yuv420p", "-movflags", "+faststart", str(out_file)
]
subprocess.run(cmd, check=True)
return out_file




if __name__ == "__main__":
from pathlib import Path
print(make_slideshow([Path("./outputs/a.jpg"), Path("./outputs/b.jpg")], Path("./outputs/out.mp4")))
