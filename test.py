import string, random

characters = string.ascii_letters


def Generate_password(n, characters):
    pwd = []
    for i in range(10):
        pwd[i] = random.choice(characters)
    return "".join(pwd)

print(Generate_password(10, characters))