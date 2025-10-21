# s = f'{n:b}'

def F(n):
    c= f'{n:b}'
    if n%2==0:
        c= '10'+c
    else:
        c= '1'+c+'01'
    r = int(c, 2)
    if r<30 :
        print(n, r)

for i in range(2000) :
    F(i)


    

