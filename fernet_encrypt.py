from cryptography.fernet import Fernet

theKey = Fernet.generate_key()

firstKey = Fernet(theKey)

print("theKey:", theKey)
print("firstKey:", firstKey)

data = "Welcome to Python Cryprography, this is LinXits!"
encrypeted_data = firstKey.encrypt(bytes(data,'utf-8'))
print ("encrypeted_data:", encrypeted_data)

decrypeted_data = firstKey.decrypt(encrypeted_data)
print("decrypeted_data:", decrypeted_data)

#byte to string
print("decrypeted_data:", decrypeted_data.decode())
