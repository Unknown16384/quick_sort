import timeit
from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pvt = arr[len(arr) // 2]
    lft = [x for x in arr if x < pvt]
    mid = [x for x in arr if x == pvt]
    rgt = [x for x in arr if x > pvt]
    return quick_sort(lft) + mid + quick_sort(rgt)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr

def compare(n):
    arr = [randint(1, 100) for _ in range(n)]
    a = timeit.timeit(lambda: quick_sort(arr), number=1000)
    b = timeit.timeit(lambda: insertion_sort(arr), number=1000)
    print(f'быстрая сортировка для списка длинной {n}  : {a}')
    print(f'сортировка вставками для списка длинной {n}: {b}')
compare(10)
compare(100)
compare(1000)
'''
вообще-то в этом примере быстрая сортировка не является особо быстрой, потому как python не оптимизирован для хвостовой рекурсии, и обычные циклы (на которых реализована сортировка вставками) работают лучше
'''