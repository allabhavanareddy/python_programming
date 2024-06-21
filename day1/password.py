n=input()
c=0
u,l,s,d=1,1,1,1
if (8-len(n)>4):
    print(8-len(n))
else:
    for i in n:
        if i.isalpha() and i.isupper():
            u=0
        elif i.isalpha() and i.islower():
            l=0
        elif not i.isalnum():
            s=0
        elif i.isdigit():
            d=0
    sum=u+l+s+d
    if sum>0:
        print(sum)
    else:
         print(-1)
    
    



        
    
    

        
    
