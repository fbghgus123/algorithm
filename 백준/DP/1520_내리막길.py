# 문제: https://www.acmicpc.net/problem/1520
# 도움된 글: https://studyandwrite.tistory.com/m/387?category=1004635
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

m, n = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0

def dfs(v):
    count = 0
    x, y = v

    if x == n-1 and y == m-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    for i in range(4):
        mx, my = x + dx[i], y + dy[i]
        if 0 <= mx < n and 0 <= my < m and Map[y][x] > Map[my][mx]:
            count += dfs((mx, my))
    dp[y][x] = count
    return dp[y][x]

print(dfs((0,0)))
