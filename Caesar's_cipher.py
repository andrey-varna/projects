print('Добро пожаловать, в программу для шифрования/дешифрования!')
def cezar(ch,sdvig):
    ordch = ord(ch)
    if 65 <= ordch <= 90:
        lg = 65
        pg = 90
        tot = 26
    elif 97 <= ordch <= 122:
        lg = 97
        pg = 122
        tot = 26
    elif 1040 <= ordch <= 1071:
        lg = 1040
        pg = 1071
        tot = 32
    elif 1072 <= ordch <= 1103:
        lg = 1072
        pg = 1103
        tot = 32
    else:
        return(ch)
    return(chr(lg + (ord(ch)-lg + sdvig)%tot))

again = 'д'

while again.lower() == 'д':
    print('Введите текст для шифрования')
    text = input()
    print('На какую величину будем делать сдвиг? Ввод значения с МИНУСОМ - дешифрует текст!')
    sdvig = int(input())
    for i in range(len(text)):
        print(cezar(text[i],sdvig),end ='')
    print()
    again = input('Еще есть текст для шифрования? Напиши "д" \n')
print('Спасибо, что были с нами. Еще увидимся...')