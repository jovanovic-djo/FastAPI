from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = False

class CreatePost(BaseModel):
    pass

class UpdatePost(BaseModel):
    title: str
    content: str
    published: bool