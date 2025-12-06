# a = 1080 * 1920 * 60 * 57 * 12 / 8
# b = 1080 * 1920 * 24 * 57 * 11 / 8

# print((a - b) / 1024)

# t = 27 * 60 + 27
# n = 28
# v = t/28 
# size = 367217732 * 332
# y=56000*15*t
# ras = size - y
# print((ras / 28)/(1024*8))

# 525481

a = (3840*2160*24 * 0.65)/(8*1024)
b = a + 120
f = 20*1024*1024
size = f//b
print(size)
r = 4320/1317
print(r)
# 1 kbyte = 1024 byte
# 1 Mbyte = 1024 kbyte
# 1 Gbyte = 1024 Mbyte
# 1 Tbyte = 1024 Gbyte