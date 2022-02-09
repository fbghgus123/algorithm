# 문제: https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

dp = [[0] * n for _ in range(2)]

dp[0][0] = a[0]

if n < 3:
    print(sum(a))

else:
    for i in range(1, 3):
        dp[0][i] = a[i] + dp[0][i-1]
        dp[1][i] = dp[0][i-1]

    for i in range(2, n):
        dp[0][i] = max(
            a[i] + a[i-1] + dp[1][i-2],
            a[i] + dp[1][i-1]
            )
        dp[1][i] = max(
            dp[0][i-1],
            dp[1][i-1]
        )
    print(max(dp[0][n-1], dp[1][n-1]))