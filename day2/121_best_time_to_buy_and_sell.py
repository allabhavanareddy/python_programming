n=list(map(int,input().split()))
max=0
b=n[0]
for i in range(len(n)):
    if n[i]<b:
        b=n[i]
    elif n[i]-b>max:
        max=n[i]-b
print(max)

