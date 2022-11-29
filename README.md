# backend
<h6 align="center" >
    Backend for <a href="https://github.com/antonio-pedro99/irctc-app"> IRCTC APP </a>. This backend was used to maintain, secure and give access to the database through RestAPI calls.
</h1>

## Inital setup for project 
    - git clone <url>
    - pip install virtualenv
    - cd backend
    - virtualenv venv
    - venv\Scripts\activate (windows)
    - source venv/bin/activate (UNIX systems)
    - pip install -r requirements.txt

## Run the backend
    - uvicorn main:app --reload
    - open http://localhost:8000/docs
## One more thing
    You need a mysql server running on your machine. Therefore, make sure you have an instance of mysql running. Furthermore, you now need to create the `railway_system` database, you can name it as per your wishes. After this, follow the steps:
     - Go to `db` and run each .sql file starting from railway_system, views, triggers, data. 
     - Go to config/db.py and change the database URL as per your configuration: your local user, password and the name of the database(e.g railway_system).
     
     Now you will be able to acess the database.
## Testing
    - open http://localhost:8000/docs
    
## Subsequent updations
    - git pull
    - venv\Scripts\activate (windows)
    - source venv/bin/activate (UNIX systems)
    - pip install -r requirements.txt

___
## rest-auth registration 
    method : POST
    url: /authenticate/rest-auth/signup/
    body: {
            "email":"",
            "username":"",
            "fullname":"",
            "password":"",
    }
    response : {
            "detail": "Verification e-mail sent."
        }
___
## rest-auth login 
    method : POST
    url: /authenticate/rest-auth/login/
    body: {
            "email": "",
            "password": "m"
        }
    response : {
            "key": "b3b7a756d27e49c29d4ae37b4c1c5782af085354",
            "user_id": 1,
    }


# End Points

### For registrations

___



# FastAPI GUIDE
https://fastapi.tiangolo.com/
# AWS GUIDE

# SQLALCHEMY GUIDE

https://docs.sqlalchemy.org/en/14/
