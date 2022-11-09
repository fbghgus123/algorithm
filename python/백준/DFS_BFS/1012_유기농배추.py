# 문제: https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input())
answer = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(v):
    global m, n
    grid[v[1]][v[0]] = 0
    for i in range(4):
        x = v[0] + dx[i]
        y = v[1] + dy[i]

        if 0 <= x < m and 0 <= y < n and grid[y][x] == 1:
            dfs((x, y))

for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    
    for i in range(m):
        for j in range(n):
            if grid[j][i] == 1:
                count += 1
                dfs((i, j))
    answer.append(count)

[print(i) for i in answer]