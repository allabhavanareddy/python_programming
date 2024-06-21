'''l1=[2,5,7,9]
l2=[1,3,6,7,18,13]
c=l1+l2
c.sort()
print(c)'''

# merge and sort the elements
l1=[2,5,7,9]
l2=[1,3,6,7,18,13]
i=0
j=0
l=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        l.append(l1[i])
        i=i+1
    else:
        l.append(l2[j])
        j=j+1
if j<len(l2):
    l.extend(l2[j:])
if i<len(l1):
    l.extend(l1[i:])
print(l)

    
    
        

    
        
        
        

    
    





