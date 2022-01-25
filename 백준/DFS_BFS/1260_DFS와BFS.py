from collections import deque

n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()

def dfs(v, visited = []):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            visited = dfs(i, visited)
    return visited

print(' '.join(list(map(str,dfs(v)))))

def bfs(v):
    visited = [v]
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(' '.join(list(map(str,bfs(v)))))
