# 1  2  3  4  5  6
# +  +  +  +  +  +
# 7  8  9 10 11 12
# =  =  =  =  =  =
# 8 10 12 14 16 18
print('напишите числа')
a=input()
#print(a, type(a))
d = a.split()
#print(d, type(d))
print('Напишите вторые числа')
b=input()
c = b.split()
v=[]
# d.extend(c)
#print(d)
for x in range(len(d)):
    #print(d[x], c[x])
    d[x]=int(d[x])
    c[x]=int(c[x])
    #print(d[x] + c[x])
    v.append(d[x]+c[x])
print(v)
