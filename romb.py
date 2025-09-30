a = int(input('vvedi chislo: '))
half = a // 2 + a % 2

for i in range(half):
    spaces =(half - i - 1)
    stars = (half + i) - spaces
    print(' ' * spaces, '*' * stars, spaces, stars)
for i in range(a-2):
    print()



# 5
# __*   spaces = 2, stars = 1
# _***  spaces = 1, stars = 3
# ***** spaces = 0, stars = 5

# 6
#   **   spaces = 2, stars = 2
#  ****  spaces = 1, stars = 4
# ****** spaces = 0, stars = 6

# 7
#    *    spaces = 3, stars = 1
#   ***   spaces = 2, stars = 3
#  *****  spaces = 1, stars = 5
# ******* spaces = 0, stars = 7