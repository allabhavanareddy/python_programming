'''ip:
    4
    t u e d
    f w o w
    r o e r
    d r u i
     word
op:
    yes'''

def fun(i,j,k,t):
    if k==len(s):
        return 1
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]:
        return
    while t!=0:
        if a[i][j]==s[k]:
            a[i][j]=0
            t=fun(i+1,j,k+1)
            t=fun(i-1,j,k+1)
            t=fun(i,j-1,k+1)
            t=fun(i,j+1,k+1)
    return t

    

n=int(input())
m=[]
for i in range(n):
    a=[]
    
    for j in range(n):
        a.append(input())
    m.append(a)
fun(i,j,k,t)
for i in range(n):
    for j in range(n):
        if a[i][j]==s[0]:
            fun(i,j,1,0)
            if c==1:
                print("yes")
                break
if c==0:
    print("no")
        
