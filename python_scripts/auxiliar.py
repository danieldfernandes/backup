import string, random

def generate_random_string(min, max):
    length = random.randint(min, max)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
