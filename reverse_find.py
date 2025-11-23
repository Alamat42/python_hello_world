# Здесь должна быть реализация функции
 
# l = [1, 2, 3, 4, 3, 2, 1]
# print(reverse_find(l, 1))
# print(reverse_find(l, 2))
# print(reverse_find(l, 3))
# print(reverse_find(l, 4))
# print(reverse_find(l, 5))

l=[1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 1, 3, 31, 31, 314, 45]
def  reverse_find(l, value):
    for i in range(len(l) -1, -1, -1):
        if l[i]==value:
            return i
    return -1

l2 = [1, 2, 3]
print(reverse_find(l, 1))
print(reverse_find(l2, 1))
print(l.index(31))
print([x for x in reversed(l)].index(31))