'''ip: f46fLK9y@56eaioJKhA
op: lowercase_vowels=4
    uv-
    lc
    uc
    digits
    special characters'''
a="aaaAAAAiiuucccBBB2244&&$$$"
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if i.isupper():
        if i in 'AEIOU':
            uv=uv+1
        else:
            uc=uc+1
    elif i.islower():
        if i in 'aeiou':
            lv=lv+1
        else:
            lc=lc+1
    elif i.isdigit():
        d=d+1
    elif not i.isalnum():
        s=s+1
print(uv)
print(uc)
print(lv)
print(lc)
print(d)
print(s)
        
        

        
    
    
    
     
    
    




