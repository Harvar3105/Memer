import aioboto3
from domain.Metadata import Metadata
from utils.config import R2_ACCESS_KEY, R2_SECRET_KEY, R2_ENDPOINT, R2_BUCKET

s3_session = aioboto3.Session(
  aws_access_key_id=R2_ACCESS_KEY,
  aws_secret_access_key=R2_SECRET_KEY,
  region_name="auto"
)

async def test_connection():
  try:
    async with s3_session.client(
    service_name="s3",
    endpoint_url=R2_ENDPOINT
    ) as s3:
      await s3.list_buckets()
      return True
  except Exception as e:
    print("Error in test_connection:", e)
    import traceback
    traceback.print_exc()
    return False

async def list_files():
  try:
    async with s3_session.client(
    service_name="s3",
    endpoint_url=R2_ENDPOINT
    ) as s3:
      paginator = s3.get_paginator("list_objects_v2")

      files: list[Metadata] = []
      async for page in paginator.paginate(Bucket=R2_BUCKET):
        for obj in page.get("Contents", []):
          files.append(Metadata(key=obj["Key"], updated_at=obj["LastModified"], url=get_file_url(obj["Key"])))

      return files
  except Exception as e:
    print("Error in list_files:", e)
    import traceback
    traceback.print_exc()
    return []

async def generate_presigned_url(key: str, expires_in_seconds: int = 3600) -> str:
  try:
    async with s3_session.client(
    service_name="s3",
    endpoint_url=R2_ENDPOINT
    ) as s3:
      return await s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
          'Bucket': R2_BUCKET,
          'Key': key
        },
        ExpiresIn=expires_in_seconds
        )
  except Exception as e:
    print("Error in list_files:", e)
    import traceback
    traceback.print_exc()
    return None

def get_file_url(key: str) -> str:
  return f"{R2_ENDPOINT}/{R2_BUCKET}/{key}"

