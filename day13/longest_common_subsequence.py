'''n="abcd"
s=[]
for i in range(len(n)):
    sb=""
    for j in range(i,len(n)):
        sb=sb+n[j]
    s.append(sb)
print(s)'''


'''program to print length of common subsequence
    a b c d
    0 0 0 0
a 0 1 1 1 1
b 0 1 2 2 2
c 0 1 2 3 3  '''


s1="abcd"
s2="abc"
u=len(s1)
v=len(s2)
m=[]
n=len(s2)+1
for i in range(len(s1)+1):
    l=[0]*n
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
s=""
while u!=0 and v!=0:
   
    if s1[u-1]==s2[v-1]:
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if m[u][v]==m[u-1][v]:
            u=u-1
print(s[::-1])

    
            
        




        