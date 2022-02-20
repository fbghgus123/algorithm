from re import A
import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize
a, e = map(int, input().split())
k = int(input())
dist = [[] for _ in range(A+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    dist[u].append((v, w))

distance = [INF] * (a+1)

distance[k] = 0
queue = []
heapq.heappush(queue, (0, k))
while queue:
    long, now = heapq.heappop(queue)
    for i in dist[now]:
        if long + i[1] < distance[i[0]]:
            distance[i[0]] = long + i[1]
            heapq.heappush(queue, (long+i[1], i[0]))
print(distance[1:])