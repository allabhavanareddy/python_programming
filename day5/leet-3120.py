n="aaAbB"
a=set(n)
print(a)
c=0
for i in a:
    if (i.islower() and i.upper() in a):
        c=c+1
print(c)
