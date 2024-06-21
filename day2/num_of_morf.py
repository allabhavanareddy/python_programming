n=input()
c=0
c1=0
for i in n:
    if i=='M':
        c=c+1
    else:
        c1=c1+1
if c==c1:
    print("0")
elif c>c1:
    print("M")
else:
    print("F")

        