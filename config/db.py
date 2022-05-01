from sqlalchemy import create_engine, MetaData
import databases
from sqlalchemy.ext.declarative import declarative_base
#change the root and the password with your own

#change the name railway_system to whatever you saved the database
DATABASE_URL = "mysql+pymysql://root:password1234@localhost:3306/railway_system"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
Base = declarative_base()