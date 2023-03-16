from sqlalchemy import create_engine, MetaData
import databases
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
#change the root and the password with your own

#change the name railway_system to whatever you saved the database
DB_USER =  config("MYSQL_USER", cast = str)
DB_PASSWORD = config("MYSQL_ROOT_PASSWORD", cast = str)
DB = config("MYSQL_DATABASE", cast = str)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:3306/{DB}"
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
Base = declarative_base()