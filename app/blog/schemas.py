from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True
        from_attributes = True

class ShowBlog(Blog):
    creator: ShowUser
    class Config:
        orm_mode = True

class ShowBlogList(BaseModel): 
    name: str
    email: str
    blogs: list[Blog]
    class Config:
        orm_mode = True
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None