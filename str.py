
a = input()

# print(a, type(a))
nums = a.split()
# print(nums, type(nums))

# int_nums = []

# for x in nums:
#     int_nums.append(int(x))

# def f(string):
#     return int(string) * 10

# int_nums_2 = [f(x) for x in nums]

# print(int_nums)
# print(int_nums_2)
b = '\n'.join(nums)
print(b, type(b))
print(1, 2, 3, 4, 5, sep = ', ', end = '\t')
print(1, 2, 3, 4, 5)

for i in range(20):
    print('*', end = '')