from fastapi import HTTPException
from blog import models
from sqlalchemy.orm import Session

from blog.hashing import Hash

def get_all_users(db: Session):
    users = db.query(models.User).all()
    return users
def get_user_by_id(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
def create_user(request: models.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def delete_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.delete(synchronize_session=False)
    db.commit()
    return {"detail": "User deleted successfully"}  
def update_user(user_id: int, request: models.User, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.update({"name": request.name, "email": request.email, "password": Hash.bcrypt(request.password)})
    db.commit()
    return "Updated successfully"   
