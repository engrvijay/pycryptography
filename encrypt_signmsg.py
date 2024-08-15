
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import utils 
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.asymmetric import padding


def signMessage(message, private_key):
    signature = private_key.sign(
                message, padding.PSS(
                         mfg = padding.MGF1(hashes.SHA256()),
                         salt_length = padding.PSS.MAX_LENGTH),
                hashes.SHA256()
                )
    return signature

def validateMessage(message, public_key):
    return public.verify( signature, message,
              padding.PSS(
                  mfg = padding.MGF1(hashes.SHA256()),
                  salt_length = padding.PSS.MAX_LENGTH),
                  hashes.SHA256()
                  )



if __name__ == '__main__':
     print("in main")
