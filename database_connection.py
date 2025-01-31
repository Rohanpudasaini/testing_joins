from fastapi import HTTPException
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session
from sqlalchemy.exc import  IntegrityError
from decouple import config
import error_constant 

#Load info from .env
host = config('host')
database = config('database')
user = config('user')
password = config('password')

# Create a connection url using SQL Alchemy's URL class
url = URL.create(
    database="testing",
    username=user,
    password=password,
    host=host,
    drivername="postgresql"
)

# create a engine with above created url
engine = create_engine(url, echo=True)

# Create a session
# TODO: make the session with context manager
session = Session(bind=engine)

#  Get session and try to commit
# If error occurs, rollback and show generic HTTPException 
def try_session_commit(session):
    try:
        session.commit()
    except IntegrityError as e:
        print(e._message())
        session.rollback()
        raise HTTPException(status_code=500,
                detail= {
                    "error":{
                        "error_type": error_constant.INTERNAL_ERROR,
                        "error_message": error_constant.INTERNAL_ERROR_MESSAGE
                        }
                    })
