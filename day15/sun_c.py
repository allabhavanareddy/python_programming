'''[3,5,9,6,8,10]
  sun falls mrng=3,5,9,10
  sun falls eveng=10'''

'''l=list(map(int,input().split(",")))
print(l)'''

arr=[3,5,9,6,11,10]
m=0
c=0
for i in range(len(arr)):
    if arr[i]>m:
        m=arr[i]
        c=c+1
    
    
m1=0
c1=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
        c1=c1+1
       
print(c,c1)
