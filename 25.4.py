from random import choice
from string import digits, ascii_lowercase, ascii_uppercase


error = ('I', 'l', 'o', 'O', '1', '0')


def generate_password(m):
    password = ""
    count = 0
    while count != m:
        flag = choice([0, 1, 2])
        if flag == 0:
            symbol = choice(ascii_lowercase)
        elif flag == 1:
            symbol = choice(digits)
        else:
            symbol = choice(ascii_uppercase)
        if symbol not in error and symbol not in password:
            password += symbol
            count += 1
    return password


def main(n, m):  # n - колтчество m - длина
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
