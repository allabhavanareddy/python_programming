'''least coins
   [1,3,4,5]
   17
   op:4(5rs-2,4rs-1,3rs-1)'''

def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if j>=i:
                if l1[j-i]!=-1:
                    if l1[j]!=-1:
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
                        
l=[1,3,4,5,6]
n=17
fun()


    

