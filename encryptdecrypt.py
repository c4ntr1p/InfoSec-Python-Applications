from cryptography.fernet import Fernet 
def write_key():

    key = Fernet.generate_key() 
    with open("key.key", "wb") as key_file: 
        key_file.write(key) 

    def load_key():
        return open("key.key", "rb").read() 
    
    write_key()
    key = load_key()
    message = "some secret message".encode() 
    f = Fernet(key) 
    encrypted = f.encrypt(message) 
    print(encrypted) 

    decrypted_encrypted = f.decrypt(encrypted) 
    print(decrypted_encrypted) 

    # project from https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python 
