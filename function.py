# Функция - именованый блок кода, который можно вызывать из любого места в программе

def hello():
    print("Hello Anton!")

def foo():
    return 42
# string to list of int
# string = '1 2 3 4'

def to_int(string):
    b = string.split()
    for x in range(len(b)):
        b[x]= int(b[x])
    return b

    
a = to_int(input())
print(sum(a))