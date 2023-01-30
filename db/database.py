# import sqlalchemy
# from databases import Database



# DATABASE_URL = 'sqlite:///application.db'
# database = Database(DATABASE_URL)
# sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


# def get_database() -> Database:
#     return 
    

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


