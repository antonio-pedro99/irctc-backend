from sqlalchemy import create_engine, MetaData
import databases
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "mysql+pymysql://admin:root1234@3.17.218.216:3306/irctc_db"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
Base = declarative_base()