a = [1, 2, 'asdf', 3.14]
b = [a, a, 10, 10, 10, 'hello']
# print(b)

# print(b.count(100))

b.append('Anton')
b.append('3.14')

# print(b)

# for x in b:
    # print(x)


a=('Напишите числа')

a = int(input())
b=[]
for i in range(a):
    i = (input())
    c=int(i)
    b.append(c)
print(b)
print(sum(b))