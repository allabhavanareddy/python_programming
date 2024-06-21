''' paths from 1st ele in matrix to last ele'''

def count_paths(i, j, c, path):
    if i < 0 or j < 0 or i >= n or j >= m or (i == k and j == 1):
        return c
    if i == n-1 and j == m-1:
        print(" -> ".join(path))
        return c + 1

    vi.append((i, j))
    path_count = c

    if (i-1, j) not in vi:
        path.append("Up")
        path_count = count_paths(i-1, j, path_count, path)
        path.pop()

    if (i, j-1) not in vi:
        path.append("Left")
        path_count = count_paths(i, j-1, path_count, path)
        path.pop()

  
    if (i+1, j) not in vi:
        path.append("Down")
        path_count = count_paths(i+1, j, path_count, path)
        path.pop()

  
    if (i, j+1) not in vi:
        path.append("Right")
        path_count = count_paths(i, j+1, path_count, path)
        path.pop()

    vi.pop()
    return path_count

n = int(input())
m = int(input())
k = int(input("blocked row index: "))

vi = []
print(count_paths(0, 0, 0, []))



