n=int(input())
pos=int(input())
c=0
for i in range(n,0,-1):
    if n%i==0:
        c=c+1
        if pos==c:
            print(i)
            break
        

    

