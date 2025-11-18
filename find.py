l = [1, 234, 10, 23, 5]
# i = 0 1 2 3 4
#

# Ищет value в списке l, и возвращает индекс найденного объект, либо возвращать -1
def find(l, value):
    for i in range(len(l)):
        if l[i] == value:
            return i
    return -1
        
print(find(l, 2))
