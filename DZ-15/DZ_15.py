# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import logging
import random
import os
import json
import inspect
from functools import wraps
import Game_ugadaj_chislo

LOWER_LIMIT = 1
UPPER_LIMIT = 100
ATT_LOWER_LIMIT = 1
ATT_LIMIT = 10
REPEAT_LIMIT = 3

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(name)-18s %(message)s',
    filename="Game_ugadaj_chislo.log",
    level=logging.INFO,
    datefmt='%H:%M:%S %d-%m-%Y',
    force=True)


def repeat(num):
    logger = logging.getLogger('repeat')
    logger.info('Начало игры')

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(num):
                print(f'Номер повтора {i+1}')
                logger.info(f'Номер повтора {i+1}')
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return inner


def get_args_str(func, *args, **kwargs) -> str:
    """
    Возвращает строку с аргументами функции, с учётом значений по умолчанию.
    Значения именованных аргументов идут в порядке, заданном в определении функции.
    Значения не заданных в определении именованных аргументов отсортированы по именам.
    Args: func: Функция, в которую передаются параметры
    Returns: Строка значений аргументов, разделённых запятыми
    """
    args_data = inspect.getfullargspec(func)
    res = []
    res.append(", ".join(map(str, args)))
    res.append(", ".join((str(kwargs.setdefault(args_data.args[len(args) + i],
                                                args_data.defaults[len(args_data.defaults) - len(args_data.args) + len(args):][i]))
                          for i in range(len(args_data.args) - len(args)))))
    res.append(", ".join((str(kwargs.setdefault(k, args_data.kwonlydefaults[k]))
                          for k in args_data.kwonlyargs)))
    res.append(", ".join((str(kwargs[k])
                          for k in sorted(kwargs.keys())
                          if k not in args_data.args + args_data.kwonlyargs)))
    return ", ".join(filter(bool, res))


def write_to_json(func):
    logger = logging.getLogger('write_to_json')

    @wraps(func)
    def wrapper(*args, **kwargs):
        f_name = func.__name__ + ".json"
        adding = True if os.path.exists(f_name) else False
        with open(f_name, "r+" if adding else "w", encoding="utf-8") as fj:
            if adding:
                json.load(fj)
                fj.seek(fj.tell() - 3)
            else:
                logger.info(f'создаём файл {f_name}')
            argsStr = get_args_str(func, *args, **kwargs)
            logger.info(f'Аргументы {argsStr =}')
            res = func(*args, **kwargs)
            logger.info(f'Результат игры {res =}')
            fj.write(("," if adding else "{")
                     + json.dumps({argsStr: res}, ensure_ascii=False, indent=2)[1:])
        return res
    return wrapper


def checkParams(func):
    logger = logging.getLogger('checkParams')

    @wraps(func)
    def wrapper(*args):
        args = list(args)
        if args[0] < LOWER_LIMIT or args[0] > UPPER_LIMIT:
            logger.warning(
                f'Верхний лимит upperLimit = {args[0]} задан вне диапазона [{LOWER_LIMIT}, {UPPER_LIMIT}]')
            args[0] = random.randint(LOWER_LIMIT, UPPER_LIMIT)
            logger.info(
                f'Верхний лимит задан случайным образом upperLimit = {args[0]}')
        if args[1] < ATT_LOWER_LIMIT or args[1] > ATT_LIMIT:
            logger.warning(
                f'Количество попыток угадать attLimit = {args[1]} задано вне диапазона [{ATT_LOWER_LIMIT}, {ATT_LIMIT}]')
            args[1] = random.randint(ATT_LOWER_LIMIT, ATT_LIMIT)
            logger.info(
                f'Количество попыток угадать задано случайным образом attLimit = {args[1]}')
        return func(*args)
    return wrapper


@repeat(REPEAT_LIMIT)
@checkParams
@write_to_json
def guessFunc(upperLimit, attLimit):
    logger = logging.getLogger('guessFunc')
    logger.info('Начало игры')
    return Game_ugadaj_chislo.game_ugadaj_chislo(LOWER_LIMIT, upperLimit, attLimit)


if __name__ == '__main__':
    # guessFunc(0, 11)
    parser = argparse.ArgumentParser(
        description=f'{REPEAT_LIMIT} раза: Угадывание числа из заданного диапазона за заданное число попыток')
    parser.add_argument('param', metavar='upperLimit attLimit', type=int,
                        nargs=2,
                        help='Введите upperLimit attLimit через разделитель - пробел')
    args = parser.parse_args()
    guessFunc(*args.param)
