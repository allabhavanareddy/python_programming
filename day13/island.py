def fun(i,j):
    if i<0 or i>=n or j<0 or j>=n or l[i][j]!=1:
        return 0
    l[i][j]=2
    ca=1
    ca=ca+fun(i+1,j)
    
    ca=ca+fun(i-1,j)

    ca=ca+fun(i,j+1)
   
    ca=ca+fun(i,j-1)
    return ca
    
l=[]        
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
m=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            k=fun(i,j)
            if k>m:
                m=k
            c=c+1
                
print(c,m)


