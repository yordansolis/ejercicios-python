import secrets
from typing import Optional
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel  # pyright: ignore[reportMissingImports]
from sqlalchemy import create_engine, Column, Integer, String  # pyright: ignore[reportMissingImports]

from sqlalchemy.orm import sessionmaker, Session  # pyright: ignore[reportMissingImports]

from sqlalchemy.orm import DeclarativeBase  # pyright: ignore[reportMissingImports]


# SQLAlchemy model
class Base(DeclarativeBase):
    pass


# This children the -> class Base(DeclarativeBase):
class DBHero(Base):  # -> Maneja la conexión con las tablas
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    secret_name = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)


# Pydantic model similar to TypeScript
class Hero(BaseModel):
    id: Optional[int] = None
    name: str
    secret_name: str
    age: Optional[int] = None


app = FastAPI()


# DATABASE SETUP
DATABASE_URL = "postgresql://estudiante:dev123@localhost:5433/dev_sql"
engine = create_engine(DATABASE_URL)

# 3. Crea las tablas en la DB basándose en los modelos (clases que heredan de Base)
Base.metadata.create_all(bind=engine)

# 4. Fábrica de sesiones - cada sesión es una "conversación" con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# autocommit=False → tú decides cuándo guardar cambios (commit)
# autoflush=False  → no envía cambios parciales automáticamente


## 5. Duplicado innecesario (se puede eliminar)
# Base.metadata.create_all(bind=engine)


# Dependency
def get_session():
    session = SessionLocal()  # 1. Abre una conexión/sesión con la DB
    try:
        yield session  # 2. "Presta" la sesión al endpoint que la necesite
    finally:
        session.close()  # 3. SIEMPRE cierra la sesión al terminar


# ✅ BIEN - con get_session() el finally SIEMPRE cierra la sesión
@app.post("/heroes/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):

    # 1. Crea un objeto Python que representa una fila en la tabla "heroes"
    # En este punto solo existe en memoria de Python, NO está en la DB todavía
    db_herp = DBHero(name=hero.name, secret_name=hero.secret_name, age=hero.age)

    # 2. Lo marca para ser insertado en la DB (lo pone "en cola")
    session.add(db_herp)

    # Ejecuta el INSERT, AHORA sí está guardado en PostgreSQL. La DB le asigna un id automáticoz
    session.commit()

    # 4. Recarga el objeto desde la DB para obtener los datos generados
    session.refresh(db_herp)

    return db_herp


@app.get("/heroes/", response_model=list[Hero])
def read_heroes(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):

    heroes = session.query(DBHero).offset(skip).limit(limit).all()

    return heroes


@app.get("/")
def read_root():
    return {"message": "Hello World"}
