def f(n):
    st = str(n)
    s = 0
    for ch in st:
        s += int(ch)
    m = int(max(st)) + int(min(st))
    l = int(st[0])
    r = int(st[-1])
    p1 = s - l
    p2 = m - r
    return int(str(min([p1, p2]), str(max([p1, p2]))))


for n in range(99999, 10000, -1):
    if f(n) == 222:
        print(n)
        break