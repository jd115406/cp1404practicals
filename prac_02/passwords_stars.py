"""
CP1404 - Get a password and display asterisks
"""
def main():
    """Get password and display asterisks"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print as many asterisks as password"""
    print("*" * len(password))


def get_password():
    """Get password ensure it's not empty"""
    password = input("Enter password: ")
    while password == "":
        print("Please enter a password")
        password = input("Enter password: ")
    return password


main()
