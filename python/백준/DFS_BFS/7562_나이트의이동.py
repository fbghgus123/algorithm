# 문제 : https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

def bfs(sx, sy, ex, ey, n):
    if sx == ex and sy == ey:
        return 0
    queue = deque()
    queue.append((sx, sy, 0))
    grid[sx][sy] = 1

    while queue:
        x, y, c = queue.popleft()
        for i in range(8):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 0:
                if dx == ex and dy == ey:
                    return c+1
                queue.append((dx, dy, c+1))
                grid[dx][dy] = 1

t = int(input())
for _ in range(t):
    i = int(input())
    grid = [[0] * i for _ in range(i)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy, ex, ey, i))

    