# 문제: https://www.acmicpc.net/problem/2468

import sys

sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
maxArea = 0
water = 0
G = max(map(max, area))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(v, water):
    for i in range(4):
        x = v[0] + dx[i]
        y = v[1] + dy[i]
        if 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and area[x][y] - water > 0:
            visited[x][y] = 1
            dfs((x, y), water)

for water in range(G):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] - water < 1 or visited[i][j] == 1:
                continue
            dfs((i,j), water)
            count += 1
    maxArea = max(maxArea,count)

print(maxArea)