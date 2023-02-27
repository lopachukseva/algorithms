def find_smallest(lst):
    smallest_element = lst[0]

    for element in lst:
        if element < smallest_element:
            smallest_element = element

    return smallest_element


def selection_sort(lst):
    new_lst = []

    while len(lst):
        smallest = find_smallest(lst)
        new_lst.append(smallest)
        lst.remove(smallest)

    return new_lst


lst = [3, 2, 1, 1, 8, 6, 88, 33, 244]

print(selection_sort(lst))
