'''ip:
    placements'''
a="placements"
b=""
for i in a:
    if i in "AEIOUaeiou":
        b=b+i.upper()
        
    else:
        b=b+i.lower()
print(b)


    
    