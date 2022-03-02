# 문제 : https://www.acmicpc.net/problem/9252

import sys
sys.setrecursionlimit(100000)

a = list(input())
b = list(input())

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
answer = []

def dfs(x, y):
    if dp[x][y] == 0:
        return
    c = [(-1, 0), (0, -1)]
    for dx, dy in c:
        cx = x + dx
        cy = y + dy
        if dp[cx][cy] == dp[x][y]:
            dfs(cx, cy)
            return
    answer.append(b[y-1])
    dfs(x-1, y-1)
dfs(len(a), len(b))

print(dp[len(a)][len(b)])
print(''.join(answer[::-1]))