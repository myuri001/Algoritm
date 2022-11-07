def invert_array(A: list):
    """
    Поменять местами значения списка
    """
    n = len(A)
    for i in range(n//2):
        A[i], A[n - 1 - i] = A[n - 1 - i], A[i]
    return A


def array_search(A: list, x: int):
    """
    Поиск числа x  в массиве lst длинною n.
    Возвращает индекс значения в массиве lst.
    Если несколько одинаковых, то вернуть первого по счету.
    Если нет то вернуть -1
    """
    n = len(A)
    for i in range(n):
        if A[i] == x:
            return i
    return -1


def left_shift(A: list):
    """
    Сдвиг влево
    """
    N = len(A)
    tmp = A[0]
    for i in range(N - 1):
        A[i] = A[i + 1]
    A[N - 1] = tmp
    return A


def right_shift(A: list):
    """
    Сдвиг вправо
    """
    N = len(A)
    tmp = A[N - 1]
    for i in range(N - 2, -1, -1):
        A[i + 1] = A[i]
    A[0] = tmp
    return A


def fib(n: int):
    """
    Выдает число фибоначчи под индексом n
    """
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


def eratosfen(n: int):
    """
    Выводит числа от 0 до n-1 и показывает какое из них простое, а какое составное
    :param n: число до которого определить какие числа состовные, а какие простые
    :return: число - составное или простое
    """
    lst = [True] * n
    lst[0] = lst[1] = False
    for i in range(2, n):
        if lst[i]:
            for m in range(2*i, n, i):
                lst[m] = False
    return [f'{k}-простое' if lst[k] else f'{k}-составное' for k in range(n)]


def stek_skobka(s: str):
    """
    Проверяет соответствие открытых и закрытых скобок по принципу стека
    """
    flag = True
    stack = []
    for lt in s:
        if lt in "({[":
            stack.append(lt)
        elif lt in ')}]':
            if len(stack) == 0:
                flag = False
                break
            bk = stack.pop()
            if bk == '(' and lt == ')':
                continue
            if bk == '[' and lt == ']':
                continue
            if bk == '{' and lt == '}':
                continue
            flag = False
            break
    if flag and len(stack) == 0:
        return 'Yes'
    else:
        return 'No'


def insert_sort(A: list) -> list:
    """
    Сортировка вставками
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A


def insert_sort2(A: list) -> list:
    """
    Сортировка вставками по Балакиреву
    """
    n = len(A)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
            else:
                break
    return A


def choise_sort(A: list):
    """
    Сортировка выбором
    """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


def bubble_sort(A: list):
    """
    Сортировка пузырьком
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A


def numer_digit(n: int) -> list:
    """
    Делит число на цифры и создает из них список

    :param n: Число состоящее из нескольких цифр
    :return: Список из цифр начиная с конца числа n
    """
    A = []
    while n:
        A.append(n % 10)
        n = n//10
    return A


def numer_digit2(n: int):
    """
    Делит число на цифры и создает из них список

    :param n: Число состоящее из нескольких цифр
    :return: Список из цифр
    """
    A = []
    while n:
        A = [n % 10] + A
        n = n//10
    return A


def gcd(a: int, b: int):
    """
    Находит наименьший общий делитель
    :param a: целочисленное число
    :param b: целочисленное число
    :return: целое число, наименьший общий делитель
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    elif b >= a:
        return gcd(a, b % a)

# Сортировка слиянием
def merge(A: list, B: list) -> list:
    """
    Соединяет два списка в третий сортируя по неубыванию
    :param A: первый список
    :param B: второй список
    :return: список С результат соединения A и B по неубыванию
    """
    C = [0] * (len(A) + len(B))
    i = 0
    k = 0
    n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n +=1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def marge_sort(A: list):
    """
    Сортировка слиянием. Разделяет список и передает в merge
    :param A: Список, который нужно отсортировать
    :return: Отсортированный список по неубыванию
    """
    if len(A) <= 1:
        return A
    middle = len(A)//2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    marge_sort(L)
    marge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    return A


def hoar_sort(A: list):
    """Сортировка Тони Хоара(Быстрая сортировка)
    Выбрать барьерный элемент, разделить на три списка: меньше барьерного, равные и больше.
    И их тоже разделить аналогично. затем соединить и записать в исходный список А
    """
    if len(A) <= 1:
        return A
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
    return A