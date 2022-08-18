# 문제: https://www.acmicpc.net/problem/2644
from collections import deque

n = int(input())
s, e = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(v):
    visited = [v]
    queue = deque()
    queue.append((v, 0))
    while queue:
        v = queue.popleft()
        if v[0] == e:
            return v[1]
        for i in graph[v[0]]:
            if i not in visited:
                queue.append((i,v[1]+1))
                visited.append(i)
    return -1

print(bfs(s))
