import logging
from pathlib import Path
from datetime import datetime


logger = logging.getLogger("auto_insta")
handler = logging.StreamHandler()
formatter = logging.Formatter(
"%(asctime)s %(levelname)s %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(20)




def timestamped_filename(prefix: str, ext: str = ".jpg") -> str:
ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
return f"{prefix}_{ts}{ext}"




def save_bytes(path: Path, data: bytes):
path.parent.mkdir(parents=True, exist_ok=True)
with open(path, "wb") as f:
f.write(data)
