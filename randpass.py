import os
import string
import random

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return password

def main():
    random_source = '/dev/random'
    random.seed(os.urandom(1024))

    password = generate_password()
    print('Generated random password: {}'.format(password))

if __name__ == '__main__':
    main()
