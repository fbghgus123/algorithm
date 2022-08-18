# 문제 : https://www.acmicpc.net/problem/2252

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
path = [[] for _ in range(n+1)]
degree = [0] * (n+1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
    degree[b] += 1

queue = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    num = queue.popleft()
    answer.append(str(num))

    for i in path[num]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)
print(' '.join(answer))

