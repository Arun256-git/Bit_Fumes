from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import authentication_router, blog_router, user_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(authentication_router.router)
app.include_router(user_router.router)
app.include_router(blog_router.router)






