# 문제: https://www.acmicpc.net/problem/1916

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, v = map(int, input().split())
    bus[s].append((e, v))
s, e = map(int, input().split())

bill = [INF] * (n+1)
bill[s] = 0

heap = []
heapq.heappush(heap, (0, s))
while heap:
    dist, now = heapq.heappop(heap)

    if bill[now] < dist:
        continue

    for next, weight in bus[now]:
        cost = dist + weight
        if cost <  bill[next]:
            bill[next] = cost
            heapq.heappush(heap, (cost, next))
print(bill[e])