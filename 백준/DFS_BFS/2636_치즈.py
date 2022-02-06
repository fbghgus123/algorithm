# 문제: https://www.acmicpc.net/problem/2636

import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int,input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
hour = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(cheese):
    a = 0
    for i in range(n):
        a += sum(cheese[i])
    return a

def melt(cheese):
    a = copy.deepcopy(cheese)
    dfs(0, 0, cheese)
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                for e in range(4):
                    x = i + dx[e]
                    y = j + dy[e]
                    if 0 <= x < n and 0 <= y < m and cheese[x][y] == 2:
                        a[i][j] = 0
                        break
    return a

def dfs(cx, cy, cheese):
    cheese[cx][cy] = 2
    for i in range(4):
        x = cx + dx[i]
        y = cy + dy[i]
        if 0 <= x < n and 0 <= y < m and cheese[x][y] == 0:
            dfs(x, y, cheese)

while check(cheese) != 0:
    hour += 1
    tmp = copy.deepcopy(cheese)
    cheese = melt(cheese)
print(hour)
print(check(tmp))