n=int(input())
t=0
for i in range(2,(n//2)+1):
    if n%i ==0:
        t=1
        break
            
if t==1:
    while(True):
        n=n+1
        t=0
        for i in range(2,(n//2)+1):
            if n%i ==0:
                t=1
                break
        if t==0:
            print(n)
            break
else:
    print(n)
    
'''n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=c+1
            break
    if c==0:
        print(n)
        break
    else:
        n=n+1'''

'''#count of prime numbers in digit
n=467765
c=0
num=0
while n:
    if n%10 in [2,3,5,7]:
        c=c+1
    n=n//10
print(c)'''
        
    
  

