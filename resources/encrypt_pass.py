import bcrypt

def encrypt_password(password: str):
    ''' Encrypt the password using bcrypt. '''
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    if not password:
        raise ValueError("password must not be empty")

    salt = bcrypt.gensalt(8)
    senha_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return senha_hash.decode('utf-8')

def valid_pass(password, hash):
    ''' Check if the password is valid. '''
    password = str(password).encode('utf-8')
    hash = str(hash).encode('utf-8')

    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False