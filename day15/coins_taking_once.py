'''coins=[2,3,5,6] taking only once
rupees:11(5rs-1,6rs-1)'''


def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(n,i-1,-1):
            if l1[j-i]!=-1:
                if l1[j]!=-1:
                    l1[j]=min(l1[i],l1[j-i]+1)
                else:
                    l1[j]=l1[j-i]+1
    print(l1[-1])
                        
l=[2,3,5,6]
n=7
fun()
