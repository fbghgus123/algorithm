# 문제: https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n+1)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        num = []
        if j != 0:
            num.append(dp[i-1][j-1] + triangle[i][j])
        if j != i:
            num.append(dp[i-1][j] + triangle[i][j])
        dp[i][j] = max(num)
print(max(dp[n-1]))