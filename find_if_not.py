l=[1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 1, 3, 31, 31, 314, 45]


def count_if_not(l, value):
    d = 0
    for i in range(len(l)):
        if l[i]!= value:
            d=d+1
    return d


l2 = [1, 1, 1, 1, 2, 2, 3]
print(count_if_not(l, 1))
print(count_if_not(l2, 5))

