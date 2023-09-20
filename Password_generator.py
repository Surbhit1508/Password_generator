import random
import string

def generate_random_string(length):
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    random_string = random_string.lower()
    return random_string

# Set the desired length of the random string
desired_length = int(input("how Long u want to be your password of the string : "))


# Generate a random string of the desired length
random_str = generate_random_string(desired_length)

print("Random String:", random_str)
