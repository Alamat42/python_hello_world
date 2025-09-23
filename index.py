a = [1, 2, 3, 4, 5, 6, 7, 8]

for x in a:
    print(x, end = ' ')

print()
print(len(a))

for i in range(len(a)):
    print('a[', i, '] = ', a[i], sep = '', end = '; ')

print()

for i in range(len(a) - 1, -1, -1):
    print(a[i], end = ' ')

b = "hello, Anton!"
print(b)

for c in b:
    print(c, end = ' ')

num = "1231234481203948"
count = 0

for c in num:
    if(c == "1"):
        count += 1

print(count)

for i in range(0, len(num), 2):
    print(i, end = ' ')

z = 12345
print(z)

for x in str(z):
    print(x, type(x))