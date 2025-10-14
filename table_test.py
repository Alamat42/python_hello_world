# a = int(input('Введите число: '))
# b = int(input('Введите второе число: ')) 
# T=[]
# L = []
# for x in range(a):
#     L.append(b)
#     T.append(L)
    
# print(T)


# 3  8
# [
#  [0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8] 
# ]

x = [i for i in range(10)]
a= int(input('Введите число: '))
# b = int(input('Введите второе число: '))
L=[]
for x in range(a):
    L.append([i+x*a for i in range(a)])

for i in range(a):
    for j in range(a):
        print(L[i][j], end = '\t')
    print()

summa = 0

for i in range(a):
    for j in range(a):
        summa += L[i][j]

print(summa)