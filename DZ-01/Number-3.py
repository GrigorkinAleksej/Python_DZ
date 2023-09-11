# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def input_natural(text, text2):
    # Ввод натурального числа
    n_str = input(text)
    while not n_str.isdigit() or n_str == '0':
        n_str = input(f'{text2}\n{text}')
    return int(n_str)


LIMIT = 100000
text2 = 'Это не является натуральным числом'
text = 'Введите натуральное число, не более '+str(LIMIT)+':\n'
num = LIMIT+1
while num > LIMIT:
    num = input_natural(text, text2)
answer = 'Число простое'
prime_numbers = []
if num == 1:
    answer = 'Единицу не относят к простым числам'
else:
    prime_numbers.append(2)
    for i in range(2, int(num**0.5)+1):
        addition = True
        for j in range(0, len(prime_numbers)):
            if num % i == 0:
                answer = 'Число составное'
                break
            elif i % prime_numbers[j] == 0:
                addition = False
                break
        if answer == 'Число составное':
            break
        if addition:
            prime_numbers.append(i)
print(answer)
