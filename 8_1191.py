def f(n):
    return f'{n:x}'

# def G(s):
#     if int(s[-1], 16) % 2 == 1 and s[0] != '1':
#         return True
#     else:
#         return False
# count = 0
# for n in range(16**4,16**5):
#     if G(f(n)):
#         count+= 1
# print(count)

count = 0
for n in range(2 * 16**4, 16**5):
    if int(f(n)[-1], 16) % 2 == 1:
        count += 1

print(count)