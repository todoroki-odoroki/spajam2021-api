from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}