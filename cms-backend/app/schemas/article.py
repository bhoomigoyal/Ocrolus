# app/schemas/article.py
from pydantic import BaseModel, ConfigDict

class ArticleBase(BaseModel):
    title: str
    content: str

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int
    author_id: int

    model_config = ConfigDict(from_attributes=True)
