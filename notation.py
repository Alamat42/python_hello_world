def Size(N):
    c=0
    while N>0:
        N = N // 10

        c+=1
        print("N = ", N, "c = ", c)

    print(c)

N = int(input())
Size(N)

# while condition :
#     # тело цикла
#     # код для повторения