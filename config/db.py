from sqlalchemy import create_engine, MetaData
import databases
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "mysql+pymysql://root:pedro23@34.123.217.251:3306/railway_system"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
Base = declarative_base()