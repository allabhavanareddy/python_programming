''' paths from 1st ele in matrix to last ele'''


'''def count(i,j,c):
    if i<0 or j<0 or i>=n or j>=m:
        return c
    if i==n-1 and j==m-1:
        c=c+1
        return c
   
    vi.append((i,j))
    if (i-1,j) not in vi:
        c=count(i-1,j,c)
    if (i,j-1) not in vi:
        c=count(i,j-1,c)
    if (i+1,j) not in vi:
        c=count(i+1,j,c)
    if (i,j+1) not in vi:
        c=count(i,j+1,c)
    vi.remove((i,j))
    return c
    
n=int(input())
m=int(input())
vi=[]
print(count(0,0,0))'''

def count_paths(i, j, path):
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    if i == n-1 and j == m-1:
        print(" -> ".join(path))
        return 1

    vi.append((i, j))
    path_count = 0
    
    if (i-1, j) not in vi:
        path.append("Up")
        path_count += count_paths(i-1, j, path)
        path.pop()

    if (i, j-1) not in vi:
        path.append("Left")
        path_count += count_paths(i, j-1, path)
        path.pop()

    if (i+1, j) not in vi:
        path.append("Down")
        path_count += count_paths(i+1, j, path)
        path.pop()

    if (i, j+1) not in vi:
        path.append("Right")
        path_count += count_paths(i, j+1, path)
        path.pop()
    
    vi.remove((i, j))
    return path_count

n = int(input())
m = int(input())
vi = []
print(count_paths(0, 0, []))



