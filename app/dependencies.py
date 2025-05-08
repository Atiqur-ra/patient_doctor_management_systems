from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app import models
from app.database import get_db
from app.config import settings
from app.crud.user import get_user_by_id


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# Get current user from token
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> models.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_id(db, user_id)
    if user is None:
        raise credentials_exception
    return user


# Ensure the user is active
def get_current_active_user(current_user: models.User = Depends(get_current_user)) -> models.User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# Patient-specific dependency
def get_current_active_patient(current_user: models.User = Depends(get_current_active_user)) -> models.User:
    if current_user.role != "patient":
        raise HTTPException(status_code=403, detail="Only patients can access this resource")
    return current_user


# Doctor-specific dependency
def get_current_active_doctor(current_user: models.User = Depends(get_current_active_user)) -> models.User:
    if current_user.role != "doctor":
        raise HTTPException(status_code=403, detail="Only doctors can access this resource")
    return current_user
