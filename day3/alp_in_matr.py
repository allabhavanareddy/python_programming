'''ip=3
      xyz
      pqr
      abc
      "xqczqb" op=yes "xaypb" op=no'''

'''n=int(input())
s=input(())
m=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    m.append(a)
print(m)

for i in range(n):
    for j in range(n):
        print(m[i][j],end="")
    print()'''

'''n=int(input())
m=[]
for i in range(n):
    m.append(input())

s=input()
f=0
for i in range(len(s)):
    if s[i] in m[i]:
        continue
    else:
        f=1
        break
if f==1:
    print("no")
else:
    print("yes")'''


n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))

s=input()
f=0
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("no")
        f=1
        break
    else:
        m[i%n].remove(s[i])
if f==0:
    print("yes")


    
    


            
    

