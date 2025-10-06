from pathlib import Path
from typing import Dict
import requests


# Simple threshold
NSFW_THRESHOLD = 0.40




def score_image(image_path: Path) -> Dict:
"""Return dict: { 'path': Path, 'score': float, 'pass': bool }
Replace with your chosen classifier. This stub assumes an HTTP API that returns {score: 0..1}
"""
api = "http://localhost:5001/score" # replace with your classifier endpoint or local call
files = {"file": open(image_path, "rb")}
r = requests.post(api, files=files, timeout=20)
r.raise_for_status()
res = r.json()
score = float(res.get("score", 1.0))
return {"path": image_path, "score": score, "pass": score < NSFW_THRESHOLD}




def filter_images(paths):
results = [score_image(p) for p in paths]
passed = [r for r in results if r["pass"]]
flagged = [r for r in results if not r["pass"]]
return passed, flagged




if __name__ == "__main__":
from pathlib import Path
print(filter_images([Path("./outputs/img_20250101.jpg")]))
