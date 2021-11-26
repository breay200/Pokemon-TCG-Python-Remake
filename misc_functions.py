import hashlib

def append_to_file(filename, text):
    #This function appends text to a file
    try:
        file = open(filename, "a")
    except IOError:
        print("Could not find file")
        return
    file.write(text + "\n")
    file.close

#could probably include in account creator class.
def hash_and_store(username, password):
    #This function hashes a password, and concatonates it with username before appending to file
    password_hash = hashlib.md5(str(password).encode('utf-8'))
    text = f"{username},{password_hash.hexdigest()}"
    append_to_file("data/passwd.txt", text)

def check_password(username, password):
    #This function checks if a username and password match the input.
    #It is used in the login functionality. Should be apart of that class!
    file = open("data/passwd.txt", "r")
    lines = file.readlines()
    match = False
    for line in lines:
        us, pwd = line.strip().split(",")
        if (username in us) and (password in pwd):
            match = True
            break
    file.close()
    return match

def check_in_file(filename, text):
    #This function checks if text is in a file
    file = open(filename, "r")
    lines = file.readlines()
    found = False
    for line in lines:
        if text in line:
            found = True
            break
    file.close()
    return found

def read_file(filename, data):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if data in line:
                return line
