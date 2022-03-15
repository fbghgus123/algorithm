# 문제 : https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

mapp = [list(map(int, list(input().strip()))) for _ in range(n)]
grid = [[[0] * m for _ in range(n)] for _ in range(2)]
grid[0][0][0] = 1
flag = True

# 0 벽 안부순 곳 1 벽 부순 곳
def bfs():
    global flag
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]

            if dx == n-1 and dy == m-1:
                    flag = False
                    print(grid[z][x][y] + 1)
                    return

            if 0 <= dx < n and 0 <= dy < m:
                if grid[z][dx][dy] == 0 and mapp[dx][dy] == 0:
                    queue.append((dx, dy, z))
                    grid[z][dx][dy] = grid[z][x][y] + 1
                if z == 0 and grid[1][dx][dy] == 0 and mapp[dx][dy] == 1:
                    queue.append((dx, dy, 1))
                    grid[1][dx][dy] = grid[0][x][y] + 1
bfs()
if n == 1 and m == 1: print(1)
elif flag: print(-1)
