import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://root:mysql_es_p3ro_Muy_buena-@localhost:3306/electrical_energy_db"
DATABASE_URL = "postgresql://numerical_user:sqCXrboVe0gT5lDAXacdFSPqocF0gK6O@dpg-csqdg1ilqhvc738emojg-a/numerical"
# DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()