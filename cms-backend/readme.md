# CMS Backend – FastAPI + PostgreSQL

A modern Content Management System backend built with FastAPI and PostgreSQL, providing robust API endpoints for content management.

##  Features

- **FastAPI Framework**: High-performance, easy-to-use Python web framework
- **PostgreSQL Database**: Reliable and scalable database solution
- **Docker Support**: Easy deployment with Docker containers
- **Interactive Documentation**: Auto-generated API documentation with Swagger UI
- **Local Development**: Support for both local and containerized development

##  Prerequisites

Before running the application, ensure you have the following installed:

### For Local Development
- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### For Docker Development
- Docker
- Docker Compose

##  Installation & Setup

### Option 1: Local Development

#### 1. Install System Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv postgresql
```

#### 2. Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Start PostgreSQL Service
```bash
sudo service postgresql start
```

#### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

### Option 2: Docker Development

#### 1. Build and Run with Docker Compose
```bash
docker compose up --build
```

##  Switching Between Local and Docker

### From Docker to Local Development
```bash
# Stop Docker containers
docker compose down

# Start PostgreSQL service
sudo service postgresql start

# Activate Python virtual environment
source venv/bin/activate

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

### From Local to Docker Development
```bash
# Deactivate Python virtual environment
deactivate

# Stop PostgreSQL service
sudo service postgresql stop

# Start Docker containers
docker-compose up --build
```

##  API Documentation

Once the application is running, you can access the interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 
##  Testing

For detailed testing instructions and screenshots, refer to our testing documentation:

 **[Testing Guide](https://docs.google.com/document/d/157_cWXomIAysrlkAUxy-9UQ1BGn37t3vozI045XUwZI/edit?tab=t.0)**

##  Project Structure

```
cms-backend/
├── alembic/                       # Alembic migration scripts
│   ├── env.py
│   ├── versions/
│   │   ├── 91b4204982bb_initial_migration.py
│   │   └── ed094139a9b9_add_bio_column_to_user.py
│   └── ... (other Alembic files)
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── config.py                  # App settings/configuration
│   ├── database.py                # Database configuration
│   ├── models/                    # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── article.py
│   ├── schemas/                   # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── article.py
│   ├── crud/                      # CRUD operations
│   │   ├── __init__.py
│   │   └── article.py
│   ├── core/                      # Core logic (auth, recently viewed, etc.)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── recently_viewed.py
│   ├── api/                       # (Optional) API route definitions
│   │   ├── __init__.py
│   │   └── articles.py
│   └── ... (other app files)
├── tests/                         # Unit and integration tests
│   ├── conftest.py
│   ├── test_article_crud.py
│   ├── test_articles.py
│   └── test_auth.py
├── requirements.txt               # Python dependencies
├── docker-compose.yml             # Docker Compose configuration
├── Dockerfile                     # Docker image definition
├── alembic.ini                    # Alembic configuration
├── .env                           # Environment variables
└── README.md                      # Project documentation
```
