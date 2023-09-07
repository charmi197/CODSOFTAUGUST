import random
import string

def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Ask the user for the desired password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Generate the password with the user-specified length
password = generate_password(length)
print("Generated Password:", password)
