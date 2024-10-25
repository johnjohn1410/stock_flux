import oracledb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

def load_credentials():
    with open('./credentials.json') as f:
        return json.load(f)

def get_db_engine():
    credentials = load_credentials()
    dsn = f"oracle+oracledb://{credentials['user']}:{credentials['password']}@{credentials['dsn']}"
    engine = create_engine(dsn, pool_size=10, max_overflow=20)
    return engine

def get_db_session():
    engine = get_db_engine()
    Session = sessionmaker(bind=engine)
    return Session()
