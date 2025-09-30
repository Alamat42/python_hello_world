# a = input().split()
# b = []
# for x in a:
#     b.append(int(x))

a = [int(x) for x in input().split()]
print(a)
a = list(map(int, input().split()))
print(a)
