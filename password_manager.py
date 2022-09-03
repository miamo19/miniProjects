from cryptography.fernet import Fernet

#funct to create the key
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""
#write_key()

#function to load the key of the encrypted password
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip('\n')
            user, passW = data.split("|")
            print("user:", user, "| password:", fer.decrypt(passW.encode()).decode())

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode  = input("World you like to add a new password or view existing ones a (view, add)? or press 'q' to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print('Invalide mode')
        continue