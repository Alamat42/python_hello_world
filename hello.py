def F(n,m):
    if n < m:
        n, m = m, n
    if n != m:
        return F(n-m, m)
    else:
        return n
    
def F2():
    n=1

    while (True):
        for m in range (1, n):
            print(n, m, F(n,m))

            if (F(n,m)>15):
                return
 
        n += 1

F2()