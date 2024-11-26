import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base, get_db
from models.user import User
from utils import hash_password, verify_password

# Configuración de base de datos en memoria
SQLALCHEMY_DATABASE_URL = "postgresql://numerical_user:sqCXrboVe0gT5lDAXacdFSPqocF0gK6O@dpg-csqdg1ilqhvc738emojg-a.oregon-postgres.render.com/numerical"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear base de datos para pruebas
Base.metadata.create_all(bind=engine)

# Sobrescribir la dependencia de la base de datos
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/register/",
        json={"email": "testuser3@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


def test_login_user():
    db = TestingSessionLocal()
    hashed_password = hash_password("securepassword2")
    db_user = User(email="testuser3@example.com", hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()

    # Intentar iniciar sesión con las credenciales correctas
    response = client.post(
        "/login/",
        json={"email": "testuser3@example.com", "password": "securepassword2"}
    )
    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["message"] == "Login successful"

    # Intentar iniciar sesión con credenciales incorrectas
    response = client.post(
        "/login/",
        json={"email": "testuser3@example.com", "password": "wrongpassword2"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}

