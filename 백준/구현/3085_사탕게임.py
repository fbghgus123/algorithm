# 문제 : https://www.acmicpc.net/problem/3085

import sys
import copy
input = sys.stdin.readline
n = int(input())

candy = [list(input().strip()) for _ in range(n)]
maxx = 0

# direction == 0 가로 1 세로
def check(x, y, direction, arr):
    tmp = [0] * n
    tmp[0] = 1

    for i in range(1, n):
        if direction == 0 and arr[x][i] == arr[x][i-1]:
            tmp[i] = tmp[i-1] + 1
        elif direction == 1 and arr[i][y] == arr[i-1][y]:
            tmp[i] = tmp[i-1] + 1
        else:
            tmp[i] = 1
    return max(tmp)

for i in range(n):
    maxx = max(maxx, check(i, 0, 0, candy))
    maxx = max(maxx, check(0, i, 1, candy))
    for j in range(n):
        if i < n-1 and candy[i][j] != candy[i+1][j]:
            grid = copy.deepcopy(candy)
            grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
            maxx = max(maxx, check(i, j, 1, grid), check(i, j, 0, grid), check(i+1, j, 0, grid))
        if j < n-1 and candy[i][j] != candy[i][j+1]:
            grid = copy.deepcopy(candy)
            grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
            maxx = max(maxx, check(i, j, 0, grid), check(i, j, 1, grid), check(i, j+1, 1, grid))
    
print(maxx)
