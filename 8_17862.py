def f(n):
    s= ''
    while n>0:
        s = f'{n %12:x}' + s
        n = n // 12
    return s


def R(s):
    count = 0
    if s.count('7') == 1:
        for x in s:
            if int(x, 12)>8:
                count += 1
        return count <= 3
    else:
        return False
    
    # if s.count('7') != 1:
    #     return False
    # for x in s:
    #     if int(x, 12)>8:
    #         count += 1
    # return count <= 3
    

count = 0
for c in range(12**4, 12**5):
    if R(f(c)):
        count+=1
print(count)