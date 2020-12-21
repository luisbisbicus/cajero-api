from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#CREANDO MOTOR Y CONEXIÓN CON LA BASE DE DATOS
DATABASE_URL = "postgresql://postgres:20142145012@localhost:5432/MISIONTIC"
engine = create_engine(DATABASE_URL)
#CREANDO LA SESIÓN
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#CREANDO BASE PARA LA CREACIÓN DE MODELOS
Base = declarative_base()
Base.metadata.schema = "cajerodb"
