# 문제 : https://www.acmicpc.net/problem/11657
# 도움된 글 : https://yabmoons.tistory.com/365

import sys
INF = sys.maxsize
n, m = map(int, input().split())
distance = [INF] * (n+1)
distance[1] = 0
graph = [[] for _ in range(n+1)]
flag = True

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(n):
    tmp = distance.copy()
    for node in range(1, n+1):
        if distance[node] == INF: continue
        for des, dis in graph[node]:
            if tmp[des] > tmp[node] + dis:
                tmp[des] = tmp[node] + dis
    if i == n-1 and tmp != distance:
        flag = False
        break
    distance = tmp

if flag:
    for i in distance[2:]:
        if i == INF:
            print(-1)
        else: print(i)
else:
    print(-1)