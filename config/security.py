from cryptography.fernet import Fernet
from schemas.user import User

key = Fernet.generate_key()
fer = Fernet(key)

def hash_password(user:User):
    user.upassword = fer.encrypt()

