'''ip="abfgresagtyuiofde"
longest substring length=12 

a=input()
d={}
s=''
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if a[i] not in s:
            s=s+a[i]
            d[s[i]]=i
        else:
            if len(s)>m:
                m=len(s)
            s=""
            break
        i=i+1
        i=d[a[i]]+1

print(m)'''


s="abfgresagtyuiofde"
b=''
c=''
m=len(b)
j=0
while(j<len(s)):
    for i in range(j,len(s)):
        if s[i] not in b:
            b=b+s[i]
        else:
            break
    if(len(b)>m):
        m=len(b)
        c=b
    b=""
    j=j+1
print(m,c)