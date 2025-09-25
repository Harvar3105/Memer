import aioboto3
import os
from domain.Metadata import Metadata

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
  try:
    async with s3_client as s3:
      paginator = s3.get_paginator("list_objects_v2")

      files: list[Metadata] = []
      async for page in paginator.paginate(Bucket=os.getenv("R2_BUCKET")):
          for obj in page.get("Contents", []):
              print(obj)
              print("\n")
              print(obj["LastModified"], type(obj["LastModified"]))
              files.append(Metadata(key=obj["Key"], updated_at=obj["LastModified"], url=get_file_url(obj["Key"])))

      print("returning files")
      return files
  except Exception as e:
        print("Error in list_files:", e)
        import traceback
        traceback.print_exc()
        return []

def get_file_url(file_name: str) -> str:
  return f"{os.getenv('R2_ENDPOINT')}/{os.getenv('R2_BUCKET')}/{file_name}"

