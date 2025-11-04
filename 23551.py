# s = f'{n:b}'

def to_str(n, base) :
    result = ''
    while n != 0 :
        result = str(n % base) + result
        n //= base
    return result

for n in range(2000):
    c = to_str(n, 2)
    if n%2==0:
        c= '10'+c
    else:
        c= '1'+c+'01'
    r = int(c, 2)
    if r<30 :
        print(n, r)



    

