from audioop import reverse
from collections import deque
n, m, v = map(int, input().split())

path = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    path[s].append(e)
    path[e].append(s)


def dfs(v):
    stack = [v]
    visited = []
    while(stack):
        current = stack.pop()
        if current in visited: continue
        visited.append(current)
        for next in path[current]:
            stack.append(next)  
    return visited

def bfs(v):
    queue = deque([v])
    visited = [v]
    while (queue):
        current = queue.popleft()
        for next in path[current]:
            if next in visited: continue
            queue.append(next)
            visited.append(next)
    return visited

[i.sort(reverse=True) for i in path]
print(*dfs(v))
[i.sort() for i in path]
print(*bfs(v))
