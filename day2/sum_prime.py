'''n=input()
m=sum(list(map(int,n)))'''

'''def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if (n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
if (n<10):
    print(pnp(n))
else:
    while(1):
        n=add(n)
        if (n<10):
            break
    print(pnp(n))
        
def dc(temp1):
    temp2=temp1
    while temp1>9:
        sum1=0
        while temp1>0:           
            rem=temp1%10
            sum1=sum1+rem
            temp1=temp1//10            
        temp1=sum1        
    prime(temp1,temp2)
def prime(temp1,temp2):
    if(temp1 in [2,3,5,7]):
        print(temp2)
    else:
        temp2=temp2+1
        dc(temp2)
n=int(input("Enter number:"))
temp1=n
dc(temp1)'''  
    
        

    

        