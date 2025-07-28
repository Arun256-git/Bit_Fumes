from typing import List
from fastapi import APIRouter,status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user_repo
from ..schemas import ShowBlogList, ShowUser, User

router = APIRouter(
    tags=['users'],
    prefix="/user"
)

@router.get("/", response_model=List[ShowBlogList], status_code=status.HTTP_200_OK)
def get_user(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user_repo.create_user(request, db)

@router.get("/{user_id}", response_model=ShowBlogList, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_repo.get_user_by_id(user_id, db)

@router.delete("/{user_id}",  tags=['users'])
def delete_user(user_id: int, db: Session = Depends(get_db)):   
    return user_repo.delete_user(user_id, db)

@router.put("/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: int, request: User, db: Session = Depends(get_db)):
   return user_repo.update_user(user_id, request, db)