# 문제: https://www.acmicpc.net/problem/14502

import sys
import copy
from collections import deque
input = sys.stdin.readline
answer = 0

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

vx = [0, 0, 1, -1]
vy = [1, -1, 0 ,0]

def bfs(tmp):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))

    while queue:
        v = queue.popleft()
        for i in range(4):
            dx = v[0] + vx[i]
            dy = v[1] + vy[i]
            if 0 <= dx < n and 0 <= dy < m and tmp[dx][dy] == 0:
                tmp[dx][dy] = 2
                queue.append((dx, dy))

    countZero = 0
    for i in tmp:
        countZero += i.count(0)
    global answer
    answer = max(answer, countZero)

def selectWall(start, a):
    if len(a) == 3:
        tmp = copy.deepcopy(grid)
        for v in a:
            tmp[v[0]][v[1]] = 1
        bfs(tmp)
    else:
        for i in range(start, n*m):
            r = i // m
            c = i % m
            if grid[r][c] == 0 and (r,c) not in a:
                selectWall(i, a+[(r,c)])

selectWall(0, [])
print(answer)
