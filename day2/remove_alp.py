n=input()
r=[]
for i in n:
    if i!='*':
        r.append(i)
    else:
        r.pop()
print(''.join(r))

    
        
        
        