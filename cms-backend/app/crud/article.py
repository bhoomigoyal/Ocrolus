
from sqlalchemy.orm import Session
from ..models.article import Article
from ..schemas.article import ArticleCreate

def create_article(db: Session, article_in: ArticleCreate, user_id: int):
    article = Article(**article_in.dict(), author_id=user_id)
    db.add(article); db.commit(); db.refresh(article)
    return article

def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def list_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()

def update_article(db: Session, article_id: int, article_in: ArticleCreate):
    article = get_article(db, article_id)
    if article:
        article.title = article_in.title
        article.content = article_in.content
        db.commit(); db.refresh(article)
    return article

def delete_article(db: Session, article_id: int):
    article = get_article(db, article_id)
    if article:
        db.delete(article); db.commit()
    return article
