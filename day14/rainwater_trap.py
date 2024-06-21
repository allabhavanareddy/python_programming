'''rainwater trapping'''
'''l=[2,5,2,3,6,7,1,0,5,7]
a=[2,5]
b=[7]
for i in range(1,len(l)-1):
    if l[i+1]<l[i]:
        l[i+1]=l[i]
    a.append(l[i+1])
for j in range(len(l)-2,-1,-1):
    if l[i]<l[i-1]:
        l[i]=l[i-1]
    b.append(l[i])
b=b[::-1]
        
print(a)
print(b)
s=0
for i in range(len(l)):
    s=s+min(a[i],b[i])-l[i]
print(s)'''

arr=[2,5,2,3,6,7,1,0,5,7]

l=[0]*len(arr)
r=[0]*len(arr)
m=0
for i in range(len(arr)):
    if arr[i]>m:
        m=arr[i]
    l[i]=m
m1=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
    r[i]=m1
s=0
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)

