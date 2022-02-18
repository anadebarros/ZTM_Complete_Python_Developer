#User inserts a username and a password and program prints the username and the length of the encrypted password

username = input("Please insert your username: ")
password = input("Please insert your password: ")

encrypted_password = "*" * len(password)

print(f"{username} your password {encrypted_password} is {len(password)} characters long")
