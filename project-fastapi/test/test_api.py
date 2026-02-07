from fastapi.testclient import TestClient
from main import DATABASE_URL, app, engine, get_session, Base, Hero
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker


# Create database de prueba 

DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()



# Anula la base de datos orginal por esta de test   -> test.db
app.dependency_overrides[get_session] = override_get_db





client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_hero():
    response = client.post(
        "/heroes/",
        json={"name": "Bruce Wayne", "secret_name": "Batman", "age": 35},
        )
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Bruce Wayne"
    assert data["secret_name"] == "Batman"
    assert data["age"] == 35
    assert "id" in data



def test_read_heroes():
    hero_id = test_create_hero()
    response = client.get(f"/heroes/{hero_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bruce Wayne"

def setup():
    Base.metadata.create_all(bind = engine)

    session = TestingSessionLocal()
    db = Hero(name="Bruce Wayne", secret_name="Batman", age=35)
    session.add(db)
    session.commit()
    session.close()

def teardown() -> None:
    Base.metadata.drop_all(bind = engine)    



