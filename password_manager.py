master_pwd = input("What is the master password? ")

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter Password: ")

    with open('password.txt', 'a' ) as f:
        f.write(name + "|" + pwd+ "\n")
def view():
    with open('password.txt', 'r' ) as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, ", password:", passw)



while True:
    mode  = input("World you like to add a new password or view existing ones a (view, add)? or press 'q' to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
        print("")
    elif mode == "add":
        add()
        print("")

    else:
        print('Invalide mode')
        continue