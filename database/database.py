from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *


SQLALCHEMY_DATABASE_URL = f"postgresql://hjgkvsqcldwomq:c1361c77630e4a9f428fa9eb77df60c8208af12765b098d7556c90692236b0aa@ec2-63-32-248-14.eu-west-1.compute.amazonaws.com:5432/d2m38cbk39p3lq"

# f"postgresql://{FSTR_DB_LOGIN}:{FSTR_DB_PASS}@{FSTR_DB_HOST}/postgres"
  

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


