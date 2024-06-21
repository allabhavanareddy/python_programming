''' ip: t5g2k1h8
        g5g8gd6h3
    op:
    865312(largest possible even number)'''

s1='t5g2k1h8'
s2='g5g8gd6h3'
l=[]
for i in s1:
    if i.isdigit() :
        l.append(i)
for i in s2:
    if i.isdigit() and i not in l:
        l.append(i)
l.sort()
l=l[::-1]

for i in range(len(l)-1,-1,-1):
    if int(l[i])%2==0:
        r=l.pop(i)
        l.append(r)
        break
result=''.join(l)
print(result)


        