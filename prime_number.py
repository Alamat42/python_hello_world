# Возвращает, является ли число простым
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Вывести все простые числа от 1 до 10000
# count = 0
# for a in range(1, 1000000):
#     if is_prime(a):
#         count+=1
# print(count)

def m(n):
    res = 1
    while n > 0:
        res *= n % 10
        n //= 10
    return res

for i in range(10):
    for j in range(10):
        n = int('31' + str(i) + '567' + str(j))
        if is_prime(n):
            print(n, m(n))