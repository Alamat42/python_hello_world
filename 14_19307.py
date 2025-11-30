def to_str(n, base):
    s = ''
    while n > 0:
        s = str(n % base) + s
        n = n // base
    return s

x = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
print(x)
print(to_str(x, 5).count('0'))