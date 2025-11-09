# 0123456789ab
def f(n):
    s=''
    while n>0:
        x = n % 12
        if x == 11:
            s = "b" + s
        elif x == 10:
            s = 'a' + s
        else:
            s=str(x)+s
        n= n // 12
    return s

# 100000 = 12 ** 5 bbbbbb = 12 ** 6

def g(s):
    if s.count('b') != 1:
        return False
    count = 0
    for x in s:
        if int(x, 12) % 2 == 0:
            count += 1

    return count == 3
    
count = 0
for n in range(12 ** 5, 12 ** 6):
    if g(f(n)):
        count += 1

print(count)

