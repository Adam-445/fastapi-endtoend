# FastAPI Project - Blog API

*A foundational project for mastering FastAPI core concepts before tackling more complex implementations*

> Developed this project while learning FastAPI as a stepping stone to more sophisticated API development. While functional, this implementation intentionally keeps scope limited to focus on fundamentals
> 

---

## Key Features

- JWT Authentication (OAuth2)
- User management system
- Post creation/editing with ownership validation
- Automated testing (90%+ coverage)
- Dockerized development/production environments
- Database migrations with Alembic
- Pydantic data validation
- CORS middleware support

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0
- **Auth**: JWT, OAuth2
- **Infra**: Docker, Docker Compose
- **Testing**: Pytest, TestClient

## Development Setup

1. Clone repo:

```bash
git clone https://github.com/Adam-445/fastapi-endtoend
cd fastapi-blog

```

1. Start containers:

```bash
docker-compose -f docker-compose-dev.yml up --build

```

1. Apply migrations:

```bash
alembic upgrade head

```

1. Access API docs: `http://localhost:8000/docs`

## Production Deployment

1. Set environment variables in `.env`:

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

1. Deploy stack:

```bash
docker-compose -f docker-compose-prod.yml up --build -d
```

## Testing

Run full test suite:

```bash
pytest -v tests/
```

---

## Project Context

This API represents my initial exploration of FastAPI ecosystem fundamentals. While functional, it primarily served as:

1. **Learning Vehicle** for:
    - First implementation of JWT authentication
    - Initial experience with SQLAlchemy relationships
    - First exposure to Alembic migrations
    - Introduction to Docker containerization
2. **Testing Ground** for:
    - Basic pytest patterns
    - Simple CI/CD concepts via Docker
    - Foundational security practices (OWASP basics)

---

## Learning Focus

Key concepts practiced in this project:

**Core FastAPI Patterns**

- Basic dependency injection
- Simple middleware configuration
- Elementary request validation

**Auth Workflows**

- First JWT implementation
- Basic OAuth2 password flow
- Initial experience with hashing

**Database Fundamentals**

- First SQLAlchemy ORM usage
- Basic migration workflows
- Simple relationship modeling

**DevOps Basics**

- Initial Docker Compose setup
- Basic multi-environment configuration
- Foundational containerization concepts
