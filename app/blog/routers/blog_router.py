from typing import List
from fastapi import APIRouter,status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user
from ..repository import blog_repo
from ..schemas import Blog, ShowBlog, User

router = APIRouter(
    tags=['blogs'],
    prefix="/blog"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog_repo.create(request, db)

@router.get("/", response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog_repo.get_all(db)

@router.get("/{blog_id}",response_model=ShowBlog, status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
   return blog_repo.get_by_id(blog_id, db)

@router.delete("/{blog_id}",tags=['blogs'])
def delete_blog(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog_repo.delete(blog_id, db)

@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog_repo.update(blog_id, request, db)
