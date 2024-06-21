n=input()
c=1
r=""
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c=c+1
        
    else:
        r=r+n[i]+str(c)
        c=1
r=r+n[-1]+str(c)
print(r)
        
        



