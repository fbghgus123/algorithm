# 문제 : https://www.acmicpc.net/problem/1238

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def djextra(start):
    time = [INF] * n
    queue = []
    heapq.heappush(queue, (0, start))
    time[start-1] = 0

    while queue:
        cost, current = heapq.heappop(queue)
        for i in road[current]:
            need = cost + i[1]
            if need < time[i[0]-1]:
                time[i[0]-1] = need
                heapq.heappush(queue, (need, i[0]))
    return time

n, m, x = map(int, input().split())
road = [[] for _ in range(n+1)]
total = [0] * (n+1)

for _ in range(m):
    s, e, cost = map(int, input().split())
    road[s].append((e, cost))

for i in range(1, n+1):
    if i == x:
        count = 1
        for j in djextra(x):
            total[count] += j
            count += 1
    total[i] += djextra(i)[x-1]
print(max(total))