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
docker-compose up --build
```

##  Switching Between Local and Docker

### From Docker to Local Development
```bash
# Stop Docker containers
docker-compose down

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
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

##  Testing

For detailed testing instructions and screenshots, refer to our testing documentation:

 **[Testing Guide](https://docs.google.com/document/d/157_cWXomIAysrlkAUxy-9UQ1BGn37t3vozI045XUwZI/edit?tab=t.0)**

##  Project Structure

```
cms-backend/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── models/          # Database models
│   ├── routes/          # API route definitions
│   ├── schemas/         # Pydantic schemas
│   └── database/        # Database configuration
├── requirements.txt     # Python dependencies
├── docker-compose.yml   # Docker configuration
├── Dockerfile          # Docker image definition
└── README.md           # This file
```
