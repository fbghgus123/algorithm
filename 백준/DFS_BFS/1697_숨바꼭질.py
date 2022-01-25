from collections import deque
n, k = map(int,input().split())
MAX = 10 ** 5
def bfs(v):
    visited = [v]
    queue = deque()
    queue.append((v,0))

    while queue:
        v = queue.popleft()
        if v[0] == k:
            return v[1]
        dx = [v[0]*2, v[0]-1, v[0]+1]
        for i in dx:
            if i == k:
                return v[1] + 1
            if i not in visited and 0 <= i <= MAX:        
                queue.append((i, v[1]+1))
                visited.append(i)

print(bfs(n))