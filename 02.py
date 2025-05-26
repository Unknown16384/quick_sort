def search_max(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    lft = search_max(arr[:mid])
    rgt = search_max(arr[mid:])
    if lft > rgt: return lft
    else: return rgt