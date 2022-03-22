# 문제 : https://www.acmicpc.net/problem/11404
# 도움된 글 : https://chanhuiseok.github.io/posts/algo-50/

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

grid = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    grid[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if grid[a][b] > c:
        grid[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if grid[i][j] == INF: grid[i][j] = 0
    print(*grid[i][1:])