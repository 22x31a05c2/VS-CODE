# login_system.py

# Dictionary to store usernames and passwords
users = {
    "admin": "password123",
    "user1": "ilovepython",
    "user2": "helloWorld"
}

def login(username, password):
    """
    Check if the username and password are correct
    """
    if username in users and users[username] == password:
        return True
    else:
        return False

def main():
    print("Welcome to the login system!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password. Try again!")

if __name__ == "__main__":
    main()