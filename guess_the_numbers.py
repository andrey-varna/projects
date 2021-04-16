import random

print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= int(a)


again = 'д'
while again.lower() == 'д':
    tot = 1
    a = input('Каким может быть максимальное загаданное число, больше нуля? \n')
    if a == 0:
        print('Введите больше нуля, пожалуйста \n')
        continue
    if not a.isdigit():
        print('Введите именно целое число, пожалуйста \n')
        continue
    else:
        x = random.randint(1, int(a))
        while True:
            print(f'Kакое число загадано от 1 до', int(a))
            n = input()
            if is_valid(n) == True:
                n = int(n)
                if n < x:
                    tot += 1
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                elif n > x:
                    tot += 1
                    print('Ваше число больше загаданного, попробуйте еще разок')
                elif n == x:
                    print('Вы угадали за ', tot, 'попыток, поздравляем!')
                    break
            else:
                print('А может быть все-таки введем целое число от 1 до ', a, '?', sep='')
    print('Спасибо, что были с нами. Еще увидимся...')
    again = input('Хочешь сыграть еще? Напиши "д" \n')