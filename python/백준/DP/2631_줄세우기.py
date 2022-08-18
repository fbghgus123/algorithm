# 문제 : https://www.acmicpc.net/problem/2631

import sys
input = sys.stdin.readline

n = int(input())
kid = []
for _ in range(n):
    kid.append(int(input()))

dp = [0] * (n+1)
for i in range(1, n):
    for j in range(i, n+1):
        if kid[i-1] < kid[j-1]:
            dp[j] = max(dp[i] + 1, dp[j])
print(n - max(dp) - 1)