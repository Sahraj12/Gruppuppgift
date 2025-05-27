from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://bankuser:secret123@localhost:5432/bankdb"

engine = create_engine(DATABASE_URL)

Base = declarative_base()
