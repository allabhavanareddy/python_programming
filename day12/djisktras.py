def bfs(s):
    d={5:9999,7:9999,4:9999,8:9999,3:9999,2:9999}
    d[s]=0
    v=[]
    q=[s]
    
    while q:
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                s=i
        
        for i in graph[s]:
            if i[0] not in v: 
                q.append(i[0])
                if d[i[0]]>i[1]+d[s]:
                    d[i[0]]=i[1]+d[s]
            
        v.append(s)
        q.remove(s)
    print(d)
    #print(v)
graph={5:[(7,2),(3,4)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]}
bfs(5)