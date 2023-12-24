from random import randint
import logging

def input_raz_plus(text2, text, flag):
    logger = logging.getLogger('input_raz_plus')
    i = True
    while flag == False:
        if i:
            num = input(text)
        else:
            num = input(f'{text2}\n{text}')
        flag = True
        for j in range(len(num)):
            if not num[j].isdigit():
                flag = False
                logger.warning(f'Введено {num} - {text2}')
                break
        i = False
    return int(num)


def game_ugadaj_chislo(LOWER_LIMIT, UPPER_LIMIT, KOL):
    logger = logging.getLogger('game_ugadaj_chislo')
    text2 = 'Это не натуральное число'
    text = 'Введите число: '
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    logger.info(f'Загадано число {num = } из диапазаона [{LOWER_LIMIT}, {UPPER_LIMIT}]')
    print(f'Загадано число от {LOWER_LIMIT} до {UPPER_LIMIT} включительно.\n'
          f'Угадай загаданное число с {KOL} попыток')
    for i in range(KOL):
        print(f'Осталось {KOL-i} попыток')
        logger.info(f'Осталось {KOL-i} попыток')
        number = UPPER_LIMIT+1
        while number > UPPER_LIMIT or number < LOWER_LIMIT:
            number = input_raz_plus(text2, text, False)
            if number > UPPER_LIMIT or number < LOWER_LIMIT:
                print('Ошибочно ввели число вне диапазона')
                logger.warning(f'Ошибочно ввели число {number = } вне диапазона')
        if num > number:
            print('больше')
            logger.info(f'введено число {number}, загаданное число БОЛЬШЕ')
        elif num < number:
            print('меньше')
            logger.info(f'введено число {number}, загаданное число МЕНЬШЕ')
        else:
            print(f'Верно. УГАДАЛ!!! с {i+1} попыток')
            logger.info(f'введено число {number}. Верно. УГАДАЛ!!! с {i+1} попыток')
            return True, num, i+1
    print(f'НЕ УГАДАЛ. Было загадоно {num}. Использованы все попытки.')
    logger.info(f'введено число {number}. НЕ УГАДАЛ. Было загадоно {num}. Использованы все попытки.')
    return False, num, i+1


if __name__ == '__main__':
    otvet = game_ugadaj_chislo(0, 1000, 10)
    print(otvet)
