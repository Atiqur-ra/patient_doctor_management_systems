import os
from uuid import uuid4
from fastapi import UploadFile
from pathlib import Path

# Define upload directory (e.g., app/uploads/)
UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Save file locally and return path
def save_file_locally(file: UploadFile) -> str:
    # Generate unique filename to prevent collisions
    file_extension = file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{file_extension}"
    file_path = UPLOAD_DIR / unique_name

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return str(file_path)
