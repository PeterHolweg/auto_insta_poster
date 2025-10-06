import base64
import requests
from pathlib import Path
from typing import List
from .config import IMAGE_API_ENDPOINT, IMAGE_MODEL, IMAGE_API_KEY, OUTPUT_FOLDER
from .utils import timestamped_filename, save_bytes


OUTPUT_FOLDER = Path(OUTPUT_FOLDER)




def generate_images(prompts, n=1) -> List[Path]:
"""Generate images for each prompt. Returns pathlib.Path list of saved image files.
This uses a placeholder JSON contract - adapt to your provider.
"""
generated_paths = []
headers = {
"Accept": "application/json",
"Authorization": f"Bearer {IMAGE_API_KEY}",
"Content-Type": "application/json",
}


for prompt in prompts:
payload = {
"model": IMAGE_MODEL,
"text_prompts": [{"text": prompt}],
"cfg_scale": 7,
"samples": n,
"steps": 28,
}
r = requests.post(IMAGE_API_ENDPOINT, headers=headers, json=payload, timeout=60)
r.raise_for_status()
data = r.json()
# provider-specific: we expect base64 artifact(s)
artifacts = data.get("artifacts", [])
for i, a in enumerate(artifacts):
b64 = a.get("base64") or a.get("b64")
image_bytes = base64.b64decode(b64)
fname = timestamped_filename("img", ".jpg")
p = OUTPUT_FOLDER / fname
save_bytes(p, image_bytes)
generated_paths.append(p)
return generated_paths




if __name__ == "__main__":
prompts = ["a tasteful fashion portrait, editorial lighting, full body, high detail"]
print(generate_images(prompts, n=2))
