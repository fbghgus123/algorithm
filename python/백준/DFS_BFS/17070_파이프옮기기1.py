# 문제: https://www.acmicpc.net/problem/17070

import sys
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(x, y, d):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return
    if d == 0 or d == 2:
        if 0 <= y+1 < n and home[x][y+1] == 0:
            dfs(x, y+1, 0)
    if d == 1 or d == 2:
        if 0 <= x+1 < n and home[x+1][y] == 0:
            dfs(x+1, y, 1)
    if 0 <= x+1 < n and 0 <= y+1 < n:
        if home[x+1][y+1] == 0 and home[x+1][y] == 0 and home[x][y+1] == 0:
            dfs(x+1, y+1, 2)
dfs(0,1,0)
print(answer)
