from app.core.config import AWS_SECRET_ACCESS_KEY
from fastapi import APIRouter, File, UploadFile
from app.dependencies.aws import s3

router = APIRouter()


@router.post("/")
async def create_file(file: bytes = File(...)):
    buckets = s3.list_buckets()
    print(s3)
    print("buckets--------", buckets)
    return {"file_size": len(file)}

@router.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}