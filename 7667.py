print('a b c d F')
def F(a, b, c, d):
    return int(((a<=b)==c)or not(d) and (d <= (not(a))))
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                print(a, b, c, d, F(a, b, c, d))