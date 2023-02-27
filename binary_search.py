def binary_search(lst, item):
    left = 0
    right = len(lst) - 1

    while left <= right:
        center = (left + right) // 2
        candidate = lst[center]
        if item == candidate:
            return center
        elif item > candidate:
            left = center + 1
        elif item < candidate:
            right = center - 1
        else:
            return None


lst = [1, 3, 4, 5, 8, 9, 11, 23, 34, 55, 66, 74, 80]
item = 80


print(binary_search(lst, item))
