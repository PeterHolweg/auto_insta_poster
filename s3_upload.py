import boto3
from botocore.client import Config
from pathlib import Path
from .config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET, S3_REGION, S3_ENDPOINT_URL




_session = boto3.session.Session()
_s3client = _session.client(
"s3",
region_name=S3_REGION,
aws_access_key_id=AWS_ACCESS_KEY_ID,
aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
endpoint_url=S3_ENDPOINT_URL if S3_ENDPOINT_URL else None,
config=Config(signature_version="s3v4")
)




def upload_file(path: Path, key: str = None, make_public: bool = True) -> str:
key = key or path.name
_s3client.upload_file(str(path), S3_BUCKET, key)
if make_public:
url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{key}"
return url
else:
# presign 7 days
return _s3client.generate_presigned_url("get_object", Params={"Bucket": S3_BUCKET, "Key": key}, ExpiresIn=604800)
