from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {"message": f"This is the blog index with limit {limit} and published status {published}."}

@app.get("/blog/unpublished")
def unpublished():
    return {"message": "This is the unpublished blog page."}

# @app.get("/about")
# def about():
#     return {"message": "This is the about page."}

@app.get("/blog/{id}")
def blog(id: int):
    return {"message": f"This is blog post {id}."}

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    return {
        "message": "Blog created successfully.",
        "blog": blog
    }

