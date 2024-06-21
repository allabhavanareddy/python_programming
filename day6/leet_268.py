'''n=list(map(int,input().split()))
for i in range(n+1):
    if i not in n:
        print(i)
        break'''
n=int(input())
l=list(map(int,input().split(' ')))
r=sum(l)
s=(n*(n+1))//2
print(s-r)