# Задача 1.
# Решить задачи, которые не успели решить на семинаре
#
# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег

def input_natural(text1, text2):
    # Ввод натурального числа
    n_str = input(text1)
    while not n_str.isdigit() or n_str == '0':
        n_str = input(f'{text2}\n{text1}')
    return int(n_str)


def oligarch(summa, k_nalog):
    # налог на богатство
    if summa > OLIGARCH:
        summa *= k_nalog
    print(f'На счёте {round(summa,2)} y.e.')
    return summa


NALOG = 10
PROZ_KOL = 3
PROZ_SN = 1.5
MIN_SN = 30
MAX_SN = 600
KRAT = 50
KOL = 3
OLIGARCH = 5_000_000
k_nalog = 1-NALOG/100
k_proz_kol = 1-PROZ_KOL/100
k_proz_sn = 1-PROZ_SN/100
text2 = 'Это не натуральное число'
summa = 0
num = 0
while True:
    summa = oligarch(summa, k_nalog)
    print(f'Ваши действия:\n'
          f'1 - пополнить\n'
          f'2 - снять\n'
          f'иное - выйти')
    play = input()
    if play == '1':
        # Пополнение
        text1 = f'Ведите сумму пополнения, кратную {KRAT}: '
        while True:
            plus = input_natural(text1, text2)
            if plus % KRAT == 0:
                summa += plus
                num += 1
                break
            else:
                print(f'Сумма пополнения должна быть кратна {KRAT}')
                summa = oligarch(summa, k_nalog)
        if num % KOL == 0:
            summa *= k_proz_kol
    elif play == '2':
        # Снятие
        text1 = f'Ведите сумму снятия, кратную {KRAT}: '
        while True:
            plus = input_natural(text1, text2)
            if plus % KRAT == 0:
                snytie_proz = plus*(1-k_proz_sn)
                if snytie_proz < MIN_SN:
                    snytie_proz = MIN_SN
                elif snytie_proz > MAX_SN:
                    snytie_proz = MAX_SN
                snytie = plus+snytie_proz
                if snytie > summa:
                    print('Недостаточно чредств на счёте')
                    break
                else:
                    summa -= snytie
                    num += 1
                    break
            else:
                print(f'Сумма снятия должна быть кратна {KRAT}')
                summa = oligarch(summa, k_nalog)
        if num % KOL == 0:
            summa *= k_proz_kol
    else:
        break
