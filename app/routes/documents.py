from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth import get_current_user
from app.database import get_db
from app.services.file_storage import save_file_locally
from app.schemas.document import DocumentCreate, DocumentOut
from app.crud import document as crud_doc
from app.models.user import User

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload", response_model=DocumentOut)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    saved_path = save_file_locally(file)
    file_type = file.content_type
    doc = DocumentCreate(file_path=saved_path, file_type=file_type, owner_id=current_user.id)
    return crud_doc.create_document(db, doc)

@router.get("/me", response_model=list[DocumentOut])
def get_my_documents(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_doc.get_user_documents(db, current_user.id)
