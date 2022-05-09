from cryptography.fernet import Fernet
from passlib.context import CryptContext
key = Fernet.generate_key()
fer = Fernet(key)

pwd_context = CryptContext(deprecated="auto", schemes=["bcrypt"])

def verify_pwd(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
   return pwd_context.hash(password)
