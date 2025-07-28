from fastapi import FastAPI
from app.blog import models
from app.blog.database import engine
from app.blog.routers import authentication_router, blog_router, user_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(authentication_router.router)
app.include_router(user_router.router)
app.include_router(blog_router.router)






