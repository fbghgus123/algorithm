# 문제 : https://www.acmicpc.net/problem/1516

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
rule = [[] for _ in range(n+1)]
cost = [0] * (n+1)
need = [0] * (n+1)
degree = [0] * (n+1)

for i in range(1, n+1):
    time, *prev, end = map(int, input().split())
    for j in prev:
        rule[j].append(i)
    degree[i] = len(prev)
    cost[i] = time

queue = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)
        need[i] = cost[i]

while queue:
    now = queue.popleft()
    for i in rule[now]:
        degree[i] -= 1
        if need[i] < need[now] + cost[i]:
            need[i] = need[now] + cost[i]
        if degree[i] == 0 :
            queue.append(i)

[print(i) for i in need[1:]]