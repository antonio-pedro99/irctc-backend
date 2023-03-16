# backend
<h6 align="center" >
    Backend for <a href="https://github.com/antonio-pedro99/irctc-app"> IRCTC APP </a>. This backend was used to maintain, secure and give access to the database through RestAPI calls.
</h1>

## Inital setup for project 
    - checkout to dev branch
    - git clone <url>
    - pip install virtualenv
    - cd backend
    - virtualenv venv
    - venv\Scripts\activate (windows)
    - source venv/bin/activate (UNIX systems)
    - pip install -r requirements.txt

## MySQL Database
    You need a mysql server running on your machine. Therefore, make sure you have an instance of mysql running. Furthermore, you now need to create the `railway_system` database, you can name it as per your wishes. After this, follow the steps:
     - Go to `db` and run each .sql file starting from railway_system, views, triggers, data. 
     - Go to your .env file and fill the parameters accordingly.
     
     Now you will be able to acess the database.
     
## Run the backend
    - uvicorn main:app --reload
    - open http://localhost:8000/docs

## Testing
    - open http://localhost:8000/docs
    
## Subsequent updations
    - git pull
    - venv\Scripts\activate (windows)
    - source venv/bin/activate (UNIX systems)
    - pip install -r requirements.txt

___
## Interactive Docs
   - open http://localhost:8000/docs
   - alternatively http://localhost:800/redoc
___

# FastAPI GUIDE
https://fastapi.tiangolo.com/
# AWS GUIDE

# SQLALCHEMY GUIDE

https://docs.sqlalchemy.org/en/14/
