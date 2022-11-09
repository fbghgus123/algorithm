# 문제 : https://www.acmicpc.net/problem/16234

import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
input = sys.stdin.readline

n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(v, num):
    global visited
    x, y = v
    visited[x][y] = num
    sum[num] += grid[x][y]
    count[num] += 1
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < n and 0 <= cy < n:
            sub = abs(grid[x][y] - grid[cx][cy])
            if l <= sub <= r and visited[cx][cy] == 0:
                dfs((cx, cy), num)
day = 0
while(1):
    sum = defaultdict(int)
    count = defaultdict(int)
    num = 1
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                dfs((i, j), num)
                num += 1
    if num > n**2:
        print(day)
        break

    for i in range(n):
        for j in range(n):
            grid[i][j] = sum[visited[i][j]] // count[visited[i][j]]
    day += 1
