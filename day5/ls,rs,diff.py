s=sum(nums)
x=0
j=0
for i in nums:
    nums[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(nums)

#xor
a=[first]
for i in range(len(encoded)):
    a.append(a[i]^encoded[i])
return a