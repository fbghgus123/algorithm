# 문제 : https://www.acmicpc.net/problem/11048

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
candy = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        candy[i][j] = max(candy[i-1][j-1], candy[i-1][j], candy[i][j-1]) + grid[i-1][j-1]

print(candy[n][m])