A = [x for x in range(100, 200 + 1)]
B = [11]

def f(y):
    C = []
    for i in range(2, y):
        if y % i == 0:
            C.append(i)

    if len(C) == 0:
        return False
    
    for x in C:
        if not ((x in C) <= ((x in A) and (x not in B))):
            return False
    
    return True

y = 2

while (True):
    if (f(y)):
        print(y)
        break
    y += 1