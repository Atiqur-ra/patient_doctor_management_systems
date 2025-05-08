from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentCreate

def create_document(db: Session, doc: DocumentCreate) -> Document:
    new_doc = Document(**doc.dict())
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def get_user_documents(db: Session, user_id: int):
    return db.query(Document).filter(Document.owner_id == user_id).all()
