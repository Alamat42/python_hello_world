# 0123456789ab
# hex
def to_str(n):
    s=''
    while n>0:
        s = f'{n % 12:x}' + s
        n= n // 12
    return s

# 100000 = 12 ** 5 bbbbbb = 12 ** 6

def condition(s):
    if s.count('b') != 1:
        return False
    count = 0
    for x in s:
        if int(x, 12) % 2 == 0:
            count += 1

    return count == 3
    
count = 0
for n in range(12 ** 5, 12 ** 6):
    if condition(to_str(n)):
        count += 1

print(count)
count = sum([int(condition(to_str(n))) for n in range(12 ** 5, 12 ** 6)])

print(count)

# 0123456789abcdef
#

