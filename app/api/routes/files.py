import datetime
from fastapi import APIRouter, File, UploadFile
import os

from app.core.config import (
    AWS_BUCKET_NAME,
    AWS_REKOGNITION_MODEL,
)
from app.dependencies.rekognition import detect_face, show_custom_labels

router = APIRouter()


@router.post("/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@router.post("/analyze")
async def create_upload_file(file: UploadFile = File(...)):
    filename = file.filename
    JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    current_time = datetime.datetime.now(JST)
    split_file_name = os.path.splitext(filename)
    file_name_unique = str(current_time.timestamp()).replace(".", "")
    file_extension = split_file_name[1]
    # data = file.file._file
    byte_data = file.file.read()
    # try:
    #     response = s3_client.upload_fileobj(data, AWS_BUCKET_NAME, file_name_unique + split_file_name[0])
    #     print("res--------", response)
    # except ClientError as e:
    #     print("err-----------", e)
    custom_labels = show_custom_labels(
        AWS_REKOGNITION_MODEL, AWS_BUCKET_NAME, byte_data
    )
    face_result = detect_face(AWS_REKOGNITION_MODEL, AWS_BUCKET_NAME, byte_data)
    emotions = face_result["Emotions"]

    return {
        "filename": file.filename,
        "emotions": emotions,
        "custom_labels": custom_labels,
    }
