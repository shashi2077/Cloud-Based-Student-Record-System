import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError

def upload_file_to_s3(file_path: str, bucket_name: str, object_key: str | None = None) -> bool:
    """Upload a file to S3. Returns True on success, False otherwise.

    Uses AWS standard environment variables:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION
    """
    object_key = object_key or os.path.basename(file_path)

    try:
        s3 = boto3.client("s3")
        s3.upload_file(file_path, bucket_name, object_key)
        return True
    except (BotoCoreError, ClientError, FileNotFoundError) as e:
        print(f"[S3] Upload failed: {e}")
        return False
