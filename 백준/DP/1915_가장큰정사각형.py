# 문제 : https://www.acmicpc.net/problem/1915

import sys
input = sys.stdin.readline
maxx = 0

n, m = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(n)]
dpx = [[0] * m for _ in range(n)]
dpy = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j == 0 and grid[i][j] == 1:
            dpx[i][j] = 1
        elif j > 0 and grid[i][j] == 1:
            dpx[i][j] = dpx[i][j-1] + 1

for i in range(m):
    for j in range(n):
        if j == 0 and grid[j][i] == 1:
            dpy[j][i] = 1
        elif j > 0 and grid[j][i] == 1:
            dpy[j][i] = dpy[j-1][i] + 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            for k in range(min(n-i, m-j)):
                if dpx[i+k][j+k] > k and dpy[i+k][j+k] > k:
                    if (k+1) ** 2 > maxx:
                        maxx = (k+1) ** 2
                else:
                    break
print(maxx)
