#to move the letter gievn positions back
n=input()
p=int(input())
s=""
for i in range(len(n)):
    if (ord(n[i])-p<=96):
        s=s+chr((ord(n[i])-p)+26)
    else:
        s=s+chr(ord(n[i])-p)
print(s)


a="bvec"
b=4
c=b%26
for i in a:
    if ((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
         d=d+chr(ord(i)-c+26)
print(d)
        



    