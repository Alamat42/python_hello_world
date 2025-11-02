a = ''.join(reversed('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))

d = dict()

for i in range(len(a)):
    d[a[i]] = i

print(d)

n = 0
for x in "информатика":
    n = n * 33 + d[x]

print(n + 1)