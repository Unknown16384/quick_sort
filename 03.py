from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pvt = arr[len(arr) // 2]
    lft = [x for x in arr if x < pvt]
    mid = [x for x in arr if x == pvt]
    rgt = [x for x in arr if x > pvt]
    return quick_sort(lft) + mid + quick_sort(rgt)

array = [randint(1, 100) for _ in range(10)]
print(array)
print(quick_sort(array))