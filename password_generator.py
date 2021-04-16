import random
print('Добро пожаловать в программу по генерации паролей')
chars = []
password = []


def generate_password(length):
    global password
    global chars
    while len(password) < length:
        password += random.choice(chars)
    random.shuffle(list(password))
    return password


def gen_chars(tot):
    global password
    global chars
    for i in range(tot):
        if ABC == 'y':
            password += random.choice(uppercase_letters)
            chars.append(uppercase_letters)
        if abc == 'y':
            password += random.choice(lowercase_letters)
            chars.append(lowercase_letters)
        if chOn == 'y':
            password += random.choice(punctuation)
            chars.append(punctuation)
        if dig == 'y':
            password += random.choice(digits)
            chars.append(digits)
        if excOn == 'y':
            for c in 'il1Lo0O':
                password = ''.join(password)
                chars = ''.join(chars)
                chars = chars.replace(c, '')
                password = password.replace(c, '')
        password = ''.join(password)
        chars = ''.join(chars)
        print(*generate_password(length), sep='')
        password = []
        chars = []


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
sim = 'il1Lo0O'
tot = int(input('Укажите количество паролей для генерации: \n'))
length = int(input('Укажите длину одного пароля, целое число: \n'))
dig = input('Включать ли цифры? (y/n) \n')
ABC = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) \n')
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) \n')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) \n')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) \n')
gen_chars(tot)