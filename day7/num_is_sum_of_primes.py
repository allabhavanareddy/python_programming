'''n=int(input())
l=[]
for i in range(2,n+1):
    f=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            f=0
            break
    if f==1:
       l.append(i)
print(l)
f=0
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==n:
            f=1
            print(l[i],l[j])
            break
    if f==1:
        break
if f==0:
    print("no")'''

def isprime(x):
    if x==1:
        return 1
    if x==2:
        return 1
    for i in range(2,(a//2)+1):
        if x%i==0:
            return 0
    return 1
a=int(input())

for i in range(1,(a//2)+1):
    if isprime(i) and isprime(a-i):
        print("yes")
        print(i,a-i)
        break
else:
    print("no")
