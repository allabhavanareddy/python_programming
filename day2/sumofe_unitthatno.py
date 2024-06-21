'''def sum(x):
    if x==0:
        return 0
    return x+fa(x-2)
      
print(sum(10))'''

def sum(x):
    if x==0:
        return 0
    return x+fa(x-2)
      
n=int(input())
if n%2==0:
    print(sum(n))
else:
    print(sum(n-1))



            
            
        