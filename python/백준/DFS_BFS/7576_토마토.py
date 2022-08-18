# 문제: https://www.acmicpc.net/problem/7576

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1


while queue:
    v = queue.popleft()
    for i in range(4):
        ci = v[0] + dx[i]
        cj = v[1] + dy[i]
        if 0 <= ci < n and 0 <= cj < m and box[ci][cj] == 0:
            visited[ci][cj] = visited[v[0]][v[1]] + 1
            box[ci][cj] = 1
            queue.append((ci, cj))

flag = False
day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            flag = True
    day = max(visited[i]) if max(visited[i]) > day else day
print(-1 if flag else day-1)