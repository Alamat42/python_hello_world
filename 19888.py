# 1024
# 128
# 16
# 2
# s = "0" + "0" + "0" + "2"
# "2000"
def F(n):
    s = ''
    while n>0:
        s= str(n%8) + s
        n = n//8
    return s
l = []
for n in range(1, 1000):
    s = F(n)
    res = ""
    if n%2 == 0:
        for x in s:
            if int(x)%2==1:
                x = '2'
            res = res + x
    if n%2 == 1:
        temp = [x for x in s]
        temp[0] = "3"
        temp[-1] = "3"
        res = ''.join(temp)
    if int(res, 8) < 300:
        l.append(int(res, 8))

print(max(l))

