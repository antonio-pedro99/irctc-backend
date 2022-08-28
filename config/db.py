from sqlalchemy import create_engine, MetaData
import databases
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "mysql+pymysql://admin:root1234@irctc-db-id.cix1p67429p1.us-east-2.rds.amazonaws.com:3306/irctc_db"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
Base = declarative_base()