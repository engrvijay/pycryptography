# secrete storage service like SSM as base64 encoded strings to preserve the formatting of keys.

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.asymmetric import padding

def utf8(s: bytes):
    return str(s, 'utf-8')


# generate ne RSA key
def rsaGetPrivateKey():
    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
            )
    return private_key

def rsaGetPublicKey(private_key: bytes):
    public_key = private_key.public_key()
    return public_key


def rsaSerializePrivateKey(private_key: bytes): 
    private_key_pem = private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.NoEncryption()
            )
    return private_key_pem


def rsaSerializePublicKey(public_key: bytes): 
    public_key_pem = public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
            )
    return public_key_pem

def createPubPEMfile(publicKey_ser):
    with open('public_key.pem', 'wb') as f:
             f.write(publicKey_ser)

def createPrivPEMfile(privateKey_ser):
    with open('private_key.pem', 'wb') as f:
             f.write(privateKey_ser)


if __name__ == '__main__':

    privateKey = rsaGetPrivateKey()
    publicKey = rsaGetPublicKey(privateKey)
    print(rsaSerializePrivateKey(privateKey))
    print(rsaSerializePublicKey(publicKey))

    privateKey_ser = rsaSerializePrivateKey(privateKey)
    publicKey_ser  = rsaSerializePublicKey(publicKey)
