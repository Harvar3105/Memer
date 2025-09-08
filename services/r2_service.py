import boto3
import os

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
    endpoint_url=os.getenv("R2_ENDPOINT")
)

def list_files(bucket_name):
    response = s3.list_objects_v2(Bucket=os.getenv("R2_BUCKET"))
    return [obj['Key'] for obj in response.get('Contents', [])]

def get_file_url(bucket_name, key):
    return f"{os.getenv("R2_ENDPOINT")}/{bucket_name}/{key}"

