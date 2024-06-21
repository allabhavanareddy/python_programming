'''import math
a=int(input())
b=int(input())
if math.gcd(a,b)==0:
    print("yes")
else:
    print("no")'''



a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2)+1):
    if a%i==0 and b%i==0:
        print("no")
        break
else:
    print("yes")

