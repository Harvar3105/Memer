import boto3
import os

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
    endpoint_url=os.getenv("R2_ENDPOINT")
)

async def list_files():
    response = await s3.list_objects_v2(Bucket=os.getenv("R2_BUCKET"))
    return [obj['Key'] for obj in response.get('Contents', [])]

def get_file_url(file_name):
    return f"{os.getenv("R2_ENDPOINT")}/{os.getenv("R2_BUCKET")}/{file_name}"

