'''l=[1,2,3,4,1,2,3,1,2]
op:[[1 2 3 4],[1 2 3],[1,2]]
l=[2,3,1,3,4,3,2]
op=[[2 3 1 4],[3 2],[3]]'''

l=[2,3,1,3,4,3,2]
m=[]
c=0
while(c!=len(l)):
    r=[]
    for i in range(len(l)):
        if (not str(l[i]).isalpha()):
            if l[i] not in r:
                c=c+1
                r.append(l[i])
                l[i]='a'
    m.append(r)
print(m)


'''a=[2,3,1,3,4,3,2]
m=[]
d={}
c=0
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(a)):
    r=[]
    for i in d:
        if d[i]!=0:
            d[i]=d[i]-1
            r.append(i)
    m.append(r)
print(m)
'''
    
   
        

    
    