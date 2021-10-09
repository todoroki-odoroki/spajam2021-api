from app.core.config import AWS_BUCKET_NAME, AWS_SECRET_ACCESS_KEY
from fastapi import APIRouter, File, UploadFile
from app.dependencies.aws import s3, bucket, s3_client
import datetime
import os
from botocore.exceptions import ClientError

from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter()


@router.post("/")
async def create_file(file: bytes = File(...)):
    print("start--------")
    # bucket = s3.Bucket(AWS_BUCKET_NAME)
    print("bucket ---------------")
    print(bucket)
    # bucket.upload_fileobj(file, "test")
    return {"file_size": len(file)}


@router.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    filename = file.filename
    JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    current_time = datetime.datetime.now(JST)
    split_file_name = os.path.splitext(filename)
    file_name_unique = str(current_time.timestamp()).replace(".", "")
    file_extension = split_file_name[1]
    data = file.file._file
    try:
        response = s3_client.upload_fileobj(data, AWS_BUCKET_NAME, file_name_unique + split_file_name[0])
        print("res--------", response)
    except ClientError as e:
        print("err-----------", e)
    return {"filename": file.filename}