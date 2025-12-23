p = [x for x in range(25, 64 + 1)]
q = [x for x in range(40, 115 + 1)]

def f(left, right):
    a = [x for x in range(left, right + 1)]
    for x in p:
        if not ((x in p) <= (((x in q) and not(x in a)) <= (x not in p))):
            return False
        
    return True

# 1 2
# [1 3]; [2 3]
# [1 4]; [2 4]; [3 4]
# [1 5]; [2 5]; [3 5] [4 5]
res = 10000
for right in range(-100, 10000):
    for left in range(-100, right):
        if f(left, right) and right - left < res:
            res = right - left
            print(right - left)
    