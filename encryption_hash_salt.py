import hashlib
import bcrypt
import scrypt

def utf8(s: bytes):
    return str(s,'utf-8')

def hashWith_sSalt(message):
    salt = b"aa1fd2d3f4d23ac44e9c5a6c3d8f9ee8c"
    hashed_message = scrypt.hash(message, salt)
    return hashed_message

def hashWith_bSalt(message):
    salt = bcrypt.gensalt()
    hashed_message = bcrypt.hashpw(message, salt)
    return hashed_message


def hashValidateMsg_bsalt(message, hashed_message_b):
    if bcrypt.checkpw(message, hashed_message_b):
        print("b- message is correct")
    else:
        print("b- Invalid message")



if __name__ == "__main__":
    hashed_message_b = hashWith_bSalt(b"password1234#$!")
    hashed_message_s = hashWith_sSalt(b"password1234#$!")
    print(hashed_message_b)
    print(hashed_message_s)
    hashValidateMsg_bsalt(b"password1234#$!", hashed_message_b)



