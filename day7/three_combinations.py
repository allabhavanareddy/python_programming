#print all three combinations from list
n=list(map(int,input().split()))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        for k in range(j+1,len(n)):
            print(n[i],n[j],n[k])





        
        
