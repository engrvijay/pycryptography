import hashlib
import bcrypt
import scrypt

def utf8(s: bytes):
    return str(s,'utf-8')

def createHash512():
    hash_obj = hashlib.sha512()
    return hash_obj 

def createHash256():
    hash_obj = hashlib.sha256()
    return hash_obj 

def updateMsgWithHash(message, hash_key):
    new_hash = hash_key.update(message)
    return new_hash


if __name__ == "__main__":
    print(createHash256().hexdigest())
    print(createHash512().hexdigest())
    print(updateMsgWithHash(b"This is message",createHash512()))




