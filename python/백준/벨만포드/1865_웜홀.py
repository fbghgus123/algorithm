# 문제 : https://www.acmicpc.net/problem/1865

import sys
input = sys.stdin.readline

INF = sys.maxsize
t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    distance[1] = 0
    flag = True
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
        graph[e].append((s, c))
    for _ in range(w):
        s, e, c = map(int, input().split())
        graph[s].append((e, -c))

    for i in range(n):
        for node in range(1, n+1):
            # if distance[node] == INF: continue
            for e, c in graph[node]:
                if distance[e] > distance[node] + c:
                    distance[e] = distance[node] + c
                    if i == n-1: flag = False
    if flag: print('NO')
    else: print('YES')