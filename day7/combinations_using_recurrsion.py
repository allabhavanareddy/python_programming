#print the given combinations using recurrsion
def combinations(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=list(map(int,input().split()))
k=int(input())
combinations(a,k)

        