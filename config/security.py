from cryptography.fernet import Fernet
from passlib.context import CryptContext
key = Fernet.generate_key()
fer = Fernet(key)


pwd_context = CryptContext(deprecated="auto", schemes=["bcrypt"])
""" def hash_password(password:str):
    return fer.encrypt(password.encode("utf-8"))

def unhash_password(hashed_password):
    return fer.decrypt(token=hashed_password).decode("utf-8") """


def verify_pwd(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
   return pwd_context.hash(password)
