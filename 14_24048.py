a = '0123456789abcdefghijklmnopqrstuvw'
k = 'kot'
g = 'golodni'
m = 'meeow'
x = 20194023088

# Функция, которая принимет строку, и основание системы счисления
# и возвращает число (int)

# base = 100
# n = 20 * 100**2 + 24 * 100**1 + 29 * 100**0
def to_int(s, base):
    n = 0
    for c in s:
        n = n * base
        n += a.index(c)
    return n

def cond(base):
    lhs = (to_int(k, base) + to_int(g, base))
    rhs = (to_int(m, base) * to_int('100', base) - x)
    return lhs == rhs

base = a.index('w')
while not cond(base):
    base += 1

print(to_int('purr', base))
# c = 'a'
# while c != 'z':
#     print(c, end = '')
#     c = chr(ord(c) + 1)

