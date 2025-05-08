from fastapi import APIRouter, UploadFile, File
from app.services.file_storage import save_file_locally

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    path = save_file_locally(file)
    return {"file_path": path}
