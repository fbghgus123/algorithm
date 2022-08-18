# 문제 : https://www.acmicpc.net/problem/2589

import sys
from collections import deque
input = sys.stdin.readline

l, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(l)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    visited = [[0] * w for _ in range(l)]
    queue = deque()
    queue.append((y, x, 1))
    maxx = 1

    while queue:
        y, x, c = queue.popleft()
        if visited[y][x] == 0 or visited[y][x] > c:
            visited[y][x] = c
            for i in range(4):
                cy = y + dy[i]
                cx = x + dx[i]
                if 0 <= cy < l and 0 <= cx < w and grid[cy][cx] == 'L':
                    if maxx < c: maxx = c
                    queue.append((cy, cx, c + 1))
    return maxx

tmp = [[0] * w for _ in range(l)]
maxx = 0
for i in range(l):
    for j in range(w):
        if grid[i][j] == 'L':
            tmp[i][j] = bfs(i, j)
            if tmp[i][j] > maxx:
                maxx = tmp[i][j]
print(maxx-1)