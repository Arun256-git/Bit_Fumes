
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import models
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from ..token import  create_access_token

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify_password(user.password,request.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    access_token = create_access_token( data={"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}