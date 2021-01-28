from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
