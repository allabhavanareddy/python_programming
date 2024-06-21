'''palindrome -number'''

'''n=int(input())
a=n
re=0
number=n
while n > 0:
    num1=n%10
    re=re*10+num1
    n=n//10

if re==number:
    print(number)
else:
   
    n=number
    while True:
        n=n+1
        nums=n
        r=0
        while nums > 0:
            num2=nums%10
            r=r*10+num2
            nums=nums//10
        if r==n:
            print(n)
            break'''


n=int(input())
m=str(n)
mid=len(m)//2
l=m[:mid]
r=m[mid:]
if l.reverse()