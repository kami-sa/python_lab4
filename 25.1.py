import random, string

error = ('I', 'l', 'o', 'O', '1', '0')


def generate_password(m):
    password = ""
    count = 0
    while count != m:
        flag = random.choice([True, False])
        if flag:
            symbol = random.choice(string.ascii_letters)
        else:
            symbol = random.choice(string.digits)
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
