from data import users

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("User already exists")
    else:
        users[username] = password
        print("Registration successful")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful")
        return username
    else:
        print("Invalid login")
        return None