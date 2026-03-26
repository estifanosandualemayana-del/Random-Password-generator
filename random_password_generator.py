import random
import string

def generate_password(length=12):
    # Combine letters, numbers, and symbols
    chars = string.ascii_letters + string.digits + string.punctuation

    # Pick random characters
    pw = ''.join(random.choice(chars) for _ in range(length))
    return pw

# main program
print("Welcome to the Password Generator.")

while True:
    length = input("\nPlease enter the desired password length: ")

    if not length.isdigit():
        print("Invalid input. Please enter a numeric value.")
        continue

    length = int(length)

    if length < 6:
        print("Warning: Passwords shorter than 6 characters may be weak.")

    print("Generated password:", generate_password(length))

    another = input("Would you like to generate another password? (y/n): ")
    if another.lower() != 'y':
        print("Thank you for using the Password Generator. Stay secure!")
        break