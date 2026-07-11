from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import crud, models
from app.database import get_db
from app.security import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    email = verify_access_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Token Inválido o expirado")
    
    usuario = crud.get_user_by_email(db, email)
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    return usuario
