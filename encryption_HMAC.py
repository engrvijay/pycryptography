import os
import hashlib
import hmac

#message example HMAC is uses symetric algoritham,
#one key

key = "TRAL-LOCO-NFID"
message = "secrete message to connect"

def createHMAC():
    h_mac = hmac.new(key.encode(),message.encode(), hashlib.sha512)
    return h_mac;


if __name__ == "__main__":
   hmac_message = createHMAC() 
   print(hmac_message.hexdigest())


