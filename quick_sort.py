def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        support_elem = array[0]
        less_elms = [x for x in array[1:] if x <= support_elem]
        greater_elms = [x for x in array[1:] if x > support_elem]
        return quick_sort(less_elms) + [support_elem] + quick_sort(greater_elms)


a = [98, 1, 0, -2, 3, 62, 11, 4, 25, 22, 45, -65]

print(quick_sort(a))
