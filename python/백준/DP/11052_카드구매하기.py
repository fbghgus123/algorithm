# 문제: https://www.acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * (n+1) for _ in range(n+1)]
card = [0] + list(map(int, input().split()))


for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            break
        dp[i][j] = card[j] + max(dp[i-j])
print(max(dp[-1]))