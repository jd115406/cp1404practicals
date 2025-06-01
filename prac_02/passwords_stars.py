def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while password == "":
        print("Please enter a password")
        password = input("Enter password: ")
    return password


main()
