# 문제: https://www.acmicpc.net/problem/10026

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
area = [list(input().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(v, type):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        if visited[v[0]][v[1]] == 0:
            visited[v[0]][v[1]] = 1
            for i in range(4):
                x = v[0] + dx[i]
                y = v[1] + dy[i]
                if 0 <= x < n and 0 <= y < n and area[x][y] == type:
                    queue.append((x, y))

count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs((i, j), area[i][j])
            count += 1

print(count, end=' ')

count = 0
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if area[i][j] == 'G': area[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs((i, j), area[i][j])
            count += 1
print(count)