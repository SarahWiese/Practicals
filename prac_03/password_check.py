"""Sarah Wiese"""

MIN_LENGTH = 5


def main():
    """Program to get and check users password"""
    print("Enter a valid password: ")
    password = input(">>> ")
    while not is_valid_password(password):
        print("Password must be {} character long".format(MIN_LENGTH))
        password = input(">>> ")
    print_asterisks(password)


def print_asterisks(password):
    """Function to print password as asterisks."""
    for i in range(len(password)+1):
        s = "*"
    print(i * s)


def get_password():
    global is_valid_password

    def is_valid_password(password):
        """Check if password is valid."""
        if len(password) < MIN_LENGTH:
            return False
            password = input(">>> ")
        return True


get_password()

main()
