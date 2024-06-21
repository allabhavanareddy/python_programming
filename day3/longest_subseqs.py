'''ip="xyzabcdefklmnopqefgh"
op=print longest substring which is in seqence
op=7 (klmnopq)'''

s=input()
c=1
m=0
for i in range(len(s)-1):
    if ord(s[i])==ord(s[i+1])-1:
        c=c+1
    else:
        if c>m:
            m=c
        c=1
if c>m:
    m=c
print(c)

    
    
    
    


