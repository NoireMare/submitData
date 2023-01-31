from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *


SQLALCHEMY_DATABASE_URL = f"postgresql://smxdzzbbdvaoim:1db005bf42c609c3f89399a710a7a2a34c37551ad69ff5178f2b258b4c17ba41@ec2-54-75-102-122.eu-west-1.compute.amazonaws.com:5432/d2ku8f5sqj67ui"

# f"postgresql://{FSTR_DB_LOGIN}:{FSTR_DB_PASS}@{FSTR_DB_HOST}:{FSTR_DB_PORT}/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


