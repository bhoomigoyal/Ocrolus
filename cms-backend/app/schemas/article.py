
# app/schemas/article.py
from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    content: str

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
