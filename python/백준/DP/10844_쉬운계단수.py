# 문제: https://www.acmicpc.net/problem/10844

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(100)]
dp[0] = [1] * 10
dp[0][0] = 0

for i in range(99):
    for j in range(0, 10):
        if dp[i][j] > 0:
            if j > 0:
                dp[i+1][j-1] += dp[i][j] % 1_000_000_000
            if j < 9:
                dp[i+1][j+1] += dp[i][j] % 1_000_000_000
print(sum(dp[n-1]) % 1_000_000_000)
            