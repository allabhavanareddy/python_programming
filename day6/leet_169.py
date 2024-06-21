'''a=input()
p= ''
m=0
for i in a:
    if a.count(i) > max:
        max = a.count(i)
        p=i
print(p)'''

a=[4,2,4,4,8,8]
c=1
p=a[0]
for i in range(1,len(a)):
    if a[i]==p:
        c=c+1
    else:
        c=c-1
        if c==0:
            c=c+1
            p=a[i]
print(p)
