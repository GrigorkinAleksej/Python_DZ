# Задача 2
# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def input_natural(text, text2):
    # Ввод натурального числа
    n_str = input(text)
    while not n_str.isdigit() or n_str == '0':
        n_str = input(f'{text2}\n{text}')
    return int(n_str)


def convert(num: int, div: int) -> str:
    # Конвертирует десятичное число в любое другое
    SYMB = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    DEC = 10
    result = ""
    if div > DEC+len(SYMB):
        result = f'Система счисления ограничена значением {DEC+len(SYMB)}'
    else:
        while num > 0:
            symb = str(num % div)
            if int(symb) >= DEC:
                symb = SYMB[int(symb)-DEC]
            result = symb + result
            num = num // div
    return result


CONTROL = 'Система'
text2 = 'Это не целое число'
text = 'Введите целое число '
num: int = input_natural(text, text2)
text = 'Введите целое число - систему счисления в которую нужно перевести десятичное число '
while True:
    div: int = input_natural(text, text2)
    res: str = convert(num, div)
    if res[:len(CONTROL)] != CONTROL:
        break
    print(res)
# Конкретно по заданию - создание строкового шестнадцатиричного значения
# и проверка на правильность конвертации с помощью функции hex.
print('0x'+res, hex(num), 'True' if '0x'+res == hex(num) else 'False')
# Универсальный вывод
print(f'Десятичное число {num} конвертируем в систему счисления {div},\
 получаем {res}')
