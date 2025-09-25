import aioboto3
import os

s3_client = aioboto3.Session(
  aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
  aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
  region_name="auto"
).client(
    service_name="s3",
    # endpoint_url=f"{os.getenv("R2_ENDPOINT")}/{os.getenv("R2_BUCKET")}"
    endpoint_url=os.getenv("R2_ENDPOINT")
    )

async def list_files():
  async with s3_client as s3:
    paginator = s3.get_paginator("list_objects_v2")

    files = []
    async for page in paginator.paginate(Bucket=os.getenv("R2_BUCKET")):
        for obj in page.get("Contents", []):
            files.append(obj["Key"])

    return files

def get_file_url(file_name):
  return f"{os.getenv('R2_ENDPOINT')}/{os.getenv('R2_BUCKET')}/{file_name}"

