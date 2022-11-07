def invert_array(A):
    """Поменять местами"""
    n = len(A)
    for i in range(n//2):
        A[i], A[n - 1 - i] = A[n - 1 - i], A[i]
    return A


def array_search(A: list, x: int):
    """ Поиск числа x  в массиве lst длинною n.
        Возвращает индекс значения в массиве lst.
        Если несколько одинаковых, то вернуть первого по счету.
        Если нет то вернуть -1
    """
    n = len(A)
    for i in range(n):
        if A[i] == x:
            return i
    return -1


def left_shift(lst, n):
    '''Сдвиг влево'''
    tmp = lst[0]
    for i in range(n-1):
        lst[i] = lst[i+1]
    lst[n-1] = tmp
    return lst


def right_shift(lst, n):
    """Сдвиг вправо"""
    tmp = lst[n-1]
    for i in range(n-2, -1, -1):
        lst[i+1] = lst[i]
    lst[0] = tmp
    return lst


def fib(n):
    '''Выдает число фибоначчи под индексом n'''
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


def eratosfen(n):
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
    """ Проверяет соответствие открытых и закрытых скобок по принципу стека"""
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


def insert_sort(A):
    ''' Сортировка вставками'''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A


def insert_sort2(a):
    """ Сортировка вставками по Балакереву"""
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            else:
                break
    return a


def choise_sort(A):
    '''Сортировка выбором'''
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


def bubble_sort(A):
    """Сортировка пузырьком"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A


def numer_digit(n):
    digit = []
    while n:
        digit.append(n%10)
        n = n//10
    return digit


def numer_digit2(n):
    digit = []
    while n:
        digit = [n%10] + digit
        n = n//10
    return digit