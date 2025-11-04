def to_8(n):
    s = ''
    while (n>0):
        s = str(n%8) + s
        n = n//8
    return s
# s = '123456'
def f(s):
    count = 0
    for x in s:
        if int(x)%2==0:
            count +=1
    if count != 2:
        return False
    if (int(s[0]) % 2 == 1) and (s[1] == '7'):
        return False
    if (int(s[-1]) % 2 == 1) and (s[-2] == '7'):
        return False
    for i in range(1, len(s) - 1):
        if int(s[i]) % 2 == 1:
            if (s[i - 1] == '7') or (s[i + 1] == '7'):
                return False
    return True


# n = int(input())
# print(to_8(n))

# 1000000 = 8 ** 6
# 7777777 = (8 ** 7) - 1
count = 0
for n in range(8 ** 6, 8 ** 7):
    if f(to_8(n)):
        count += 1

print(count)