from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .models.user import User
from .models.article import Article
from .schemas.user import UserCreate, UserResponse
from .schemas.article import ArticleCreate, ArticleResponse
from .core.auth import hash_password, create_access_token, get_current_user, verify_password
from .core.recently_viewed import recent_views
from .crud.article import create_article, get_article, list_articles, update_article, delete_article

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# Setup OpenAPI so Swagger shows JWT auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="CMS Backend",
        version="1.0.0",
        description="Content Management System API with JWT auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Auth routes
@app.post("/auth/register", response_model=UserResponse)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(user_in.password)
    user = User(username=user_in.username, email=user_in.email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/auth/login")
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_in.username).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    token = create_access_token({"user_id": user.id})
    return {"access_token": token}

# Article routes
@app.post(
    "/articles/",
    response_model=ArticleResponse,
    dependencies=[Depends(get_current_user)],
    openapi_extra={"security": [{"BearerAuth": []}]}
)
def api_create(article: ArticleCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return create_article(db, article, user.id)

@app.get("/articles/", response_model=list[ArticleResponse])
def api_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_articles(db, skip, limit)

@app.get("/articles/{article_id}", response_model=ArticleResponse)
def api_get(article_id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    art = get_article(db, article_id)
    if not art:
        raise HTTPException(status_code=404, detail="Article not found")
    recent_views.add(user.id, article_id)
    return art

@app.put("/articles/{article_id}", response_model=ArticleResponse)
def api_update(article_id: int, article: ArticleCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    art = get_article(db, article_id)
    if not art or art.author_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return update_article(db, article_id, article)

@app.delete("/articles/{article_id}")
def api_delete(article_id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    art = get_article(db, article_id)
    if not art or art.author_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    delete_article(db, article_id)
    return {"detail": "Deleted"}

# Recently viewed
@app.get("/users/me/recently-viewed", response_model=list[int])
def api_recent(user=Depends(get_current_user)):
    return recent_views.get(user.id)
