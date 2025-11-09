# 'ВЬЮГА'
# '01234'
# от 000000 до 444444
# 444444 = 5 ** 6 - 1
# Найти все, в которых есть '23'

hw = 'hello world'
h = 'hello'
if h in hw:
    print("True")
else:
    print("False")

def f(n):
    s=''
    while n>0:
        s=str(n%5)+s
        n= n // 5
    return s

d=0
for n in range(0, 5 ** 6):
    a=f(n)
    if '23' in a:
        d+=1

print(d)

        
