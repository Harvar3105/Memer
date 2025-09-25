import aioboto3
import os

# def s3_client():
#   return aioboto3.client(
#     service_name='s3',
#     aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
#     aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
#     endpoint_url=os.getenv("R2_ENDPOINT")
#   )

s3_client = aioboto3.Session(
  aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
  aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
  region_name="auto"
).client(
    service_name="s3",
    endpoint_url=f"{os.getenv("R2_ENDPOINT")}/{os.getenv("R2_BUCKET")}"
    )

async def list_files():
  print("Listing files start")
  print(s3_client)
  print(os.getenv("R2_ENDPOINT"))
  print(os.getenv("R2_BUCKET"))
  async with s3_client as s3:
    print("Requesting response")
    paginator = s3.get_paginator("list_objects_v2")
    print(paginator)

    files = []
    async for page in paginator.paginate(Bucket=os.getenv("R2_BUCKET")):
        for obj in page.get("Contents", []):
            files.append(obj["Key"])

    return files

    # response = await s3.list_objects_v2()
    # print(response)
    # return [obj['Key'] for obj in response.get('Contents', [])]

def get_file_url(file_name):
  return f"{os.getenv('R2_ENDPOINT')}/{os.getenv('R2_BUCKET')}/{file_name}"

