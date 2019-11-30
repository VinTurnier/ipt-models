import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



connection_string = os.environ.get('IPT_CONNECTION_STRING')
def get_connection_string(connection_string):
    if connection_string is None:
        raise Exception('IPT_CONNECTION_STRING cannot be Null')
    else:
        return connection_string

engine = create_engine(get_connection_string(connection_string))
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
