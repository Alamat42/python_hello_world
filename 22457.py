def Size(N):
    c=0
    while N>0:
        N = N // 7
        c+= 1
    return c

def Sum(N):
    s = 0
    while N>0:
        s+=N%7
        N = N // 7
    return s

for N in range(1, 100000):
    R = 0
    if Sum(N) % 2 == 0:
        R = N * 7**3 + 5 + 5 * 7 + 5 * 7**2
    else:
        R = (3 + 3 * 7) * 7**Size(N) + N
        R= R * 7**1 + 6

    if R < 12717 :
        print(N, R)
    



  
