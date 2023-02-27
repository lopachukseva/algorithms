def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + high
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = [3, 5, 7, 8, 9, 11, 12, 23, 33, 45, 56, 89]
item = 11

print(binary_search(lst, item))
