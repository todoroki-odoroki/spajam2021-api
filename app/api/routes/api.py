from fastapi import APIRouter

from app.api.routes import example, files

router = APIRouter()
router.include_router(example.router, tags=["example"], prefix="/examples")
router.include_router(files.router, tags=["files"], prefix="/files")


@router.get("/")
async def hello():
    return {"text": "hello"}
