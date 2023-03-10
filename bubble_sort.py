def bubble_sort(lst):
    iterations_count = len(lst)

    for _ in range(1, iterations_count):
        for j in range(1, len(lst)):
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


nums_list = [51, 1, 3, -6, 5, 10, 4, 0, 19]

bubble_sort(nums_list)

print(nums_list)
