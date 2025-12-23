p = [x for x in range(10, 150 + 1)]
q = [x for x in range(160, 250 + 1)]
r = [x for x in range(240, 300 + 1)]

def f(left, right):
    a = [x for x in range(left, right)]
    for x in q:
        if not (((x not in a) <= (x in r))):
            return False
    return True

min = 10000
for right in range(0, 10000):
    for left in range(0, right):
        if f(left, right):
            if right - left < min:
                min = right - left
                print(right - left)
# r = 1, l = 0
# r = 2, l = 0
# r = 2, l = 1
# r = 3, l = 0
# r = 3, l = 1
# r = 3, l = 2     

# for y in range(x, a):
#     if ((x in q) <= (x in p) or (not(x in a) <= (x in r)))
# ((x in q) <= (x in p) or (not(x in a) <= (x in r)))

# l = (x in q)
# r = (x in p) or (not(x in a) <= (x in r))

# l <= r

# eсли l == 0 и r == 0 то (l <= r) == True
# eсли l == 0 и r == 1 то (l <= r) == True

# eсли l == 1 и r == 0 то (l <= r) == False
# eсли l == 1 и r == 1 то (l <= r) == True