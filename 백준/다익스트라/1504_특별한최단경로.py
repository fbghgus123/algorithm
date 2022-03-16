# 문제 : https://www.acmicpc.net/problem/1504

import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
path = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    path[a].append((b, c))
    path[b].append((a, c))
v1, v2 = map(int, input().split())

def diextra(start, end):
    cost = [10**6] * (n+1)
    cost[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        price, current = heapq.heappop(queue)
        for i in path[current]:
            total = cost[current] + i[1]
            if cost[i[0]] > total:
                cost[i[0]] = total
                heapq.heappush(queue, (i[1], i[0]))
    return cost[end]
a = -1
a1 = diextra(1, v1)
a2 = diextra(v1, v2)
a3 = diextra(v2, n)
if a1 < 10 ** 6 and a2 < 10 ** 6 and a3 < 10 ** 6:
    a = a1 + a2 + a3

b = -1
b1 = diextra(1, v2)
b2 = diextra(v2, v1)
b3 = diextra(v1, n)
if b1 < 10 ** 6 and b2 < 10 ** 6 and b3 < 10 ** 6:
    b = b1 + b2 + b3

if a == -1 and b != -1:
    print(b)
elif a != -1 and b == -1:
    print(a)
else:
    print(min(a, b))