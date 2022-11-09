# 문제: https://www.acmicpc.net/problem/2294

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(k+1):
    dp[0][i] = 100_000

for i in range(1, n+1):
    for j in range(1, k+1):
        if j - coin[i-1] >= 0:
            dp[i][j] = min(dp[i][j-coin[i-1]] + 1, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
if dp[n][k] == 100_000:
    print(-1)
else:
    print(dp[n][k])