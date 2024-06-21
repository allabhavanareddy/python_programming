'''n=school
p=3
l 2 --->hoolsc
r 3 --->oolsch
l 1 --->chools
hoc
'''
a=input()
n=int(input())
str=[]
for i in range(n):
    b=input()
    if b[0]=='L':
        str.append([a[int(b[2])]])
    else:
        str.append([-int(b[2])])
print(str)
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    
    b.append(t)
print(b)
print(str)
for i in b:
    if i==str:
        print("yes")
        break
else:
    print("no")
        
