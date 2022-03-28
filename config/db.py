from sqlalchemy import create_engine, MetaData
import databases

DATABASE_URL = "mysql+pymysql://root:password1234@localhost:3306/railway_system"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
