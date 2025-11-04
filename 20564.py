print('x y w z F')
def F(x, y, w, z):
    return int(x and ((w <= y)==z))

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(x, y, w, z, F(x, y, w, z))


# x y w z F             1   2   3   4
# 1 0 1 0 1                 w    z    y
# 1 0 0 1 1
# 0 1 1 1 0

# x y w z F
# 0 1 1 1 0
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 1 1 0
# 1 1 1 0 0

# x y w z F                 1   2    3      4
# 1 0 0 1 1                 z   x    w      y
# 1 0 1 0 1
# 1 1 1 0 0
