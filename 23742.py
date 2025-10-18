def R(N):
    x = N % 3
    if x == 0 :
        y = N % (2 ** 3)
        N = N * (2 ** 3) + y
        # 1101 * 1000 = 1101000
    elif x == 1:
        N = N * (2 ** 2) + x * 3
    else :
        N = N * (2 ** 3) + x * 3

    return N

a = 0

while(R(a) < 200) :
    a += 1

print(a)