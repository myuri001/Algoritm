def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

# print(fib1(40))

cache = {}
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib1(n - 1) + fib1(n - 2)
    return cache[n]
# print(fib2(50))


def memo(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

f = memo(fib1)
# print(f(40))


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1

# print(fib3(8000))

import time

def timed(f, *args, n_iter=100): #
    """Измеряет время работы функций
    Принимет функцию f, ее аргументы, опциональное количество раз измерений n_iter"""
    acc = float('inf')   # аккумулятор хранит минимальное измеренное время работы
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)    # Обновим аккумулятор, если время меньше, чем уже измеренное
    return acc
# timed(fib3, 800)

from matplotlib import pyplot as plt

def compare(fs, args):
    """"Строит графики, принимает функции которые надо сравнить и их аргументы
    """
    for f in fs:    # Строит график для каждой функции
        # по оси x отложены аргументы args, по оси y врем работы функций f для каждой из аргументов
        plt.plot(args, [timed(f, arg) for arg in args ], label=f.__name__)

    plt.legend()    # Легенда
    plt.grid(True)    # Сетка
    plt.show()


# compare([fib1, fib3], list(range(20)))

import random
def test(gcd, n_iter=100):
    """ Тест функции на корректность"""
    for i in range(n_iter):
        c = random.randint(0, 1024)    # Сгенерируем случайное число
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1    # Делитель только 1, других нет
        d = gcd(a, b)    # Наименьший общий делитель
        assert a % d == b % d == 0    # Проверим, что делитель правильный и делится без остатка


def gcd1(a, b):
    """ Итеративная наивная версия алгоритма Евклида"""
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):    # Перебираем кандидатов в делители в обратном порядке
        if d == 0 or a % d == b % d == 0:    # Так как перебор с максимального, то наибольший общий делитель будет первое число
            return d


# test(gcd1)

def gcd2(a, b):
    """Альтернативная версия алгоритма Евклида"""
    assert a >= 0 and b >= 0
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

# print(gcd2(1010100100101, 101001001001010))

def gcd3(a, b):
    """Рекурсивная версия алгоритма Евклида"""
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)

def gcd4(a, b):
    """Альтернативный Рекурсивная версия алгоритма Евклида"""
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)












