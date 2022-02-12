# 문제: https://www.acmicpc.net/problem/1753
# 도움된 글: https://resilient-923.tistory.com/335

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    path = tuple(map(int, input().split()))
    graph[path[0]].append((path[1], path[2]))

distance = [INF] * (v+1)

queue = []
distance[k] = 0
heapq.heappush(queue, (0, k))

while queue:
    dist, now = heapq.heappop(queue)
    for next, weight in graph[now]:
        cost = dist + weight
        if cost <  distance[next]:
            distance[next] = cost
            heapq.heappush(queue, (cost, next))
[print(i if i != INF else 'INF') for i in distance[1:]]
        

