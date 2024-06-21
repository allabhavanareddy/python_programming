def even(x,s):
    if x==len(a):
        return s
    if a[x]%2==0:
        s=s+a[x]
    return even(x+1,s)
def odd(x,s):
    if x==len(a):
        return s
    if b[x]%2==1:
        s=s+b[x]
    return odd(x+1,s)
        
a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(even(0,0),odd(0,0))

            
            
        
    