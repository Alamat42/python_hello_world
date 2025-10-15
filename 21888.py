

# def sqr(x) :
#     return x * x
# ^ and
# v or
def F(x, y, w, z):
    return int(x and (not(y)) or (y == z) or  (w))

print('x y w z F')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(x, y, w, z, F(x, y, w, z))


# x y w z F             1  2  3  4 
# 0 0 0 1 0             x  w  z  y
# 0 1 0 0 0
# 1 1 0 0 0

