# 문제 : https://www.acmicpc.net/status?user_id=fbghgus123&problem_id=15486&from_mine=1

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

schedule = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    cost, value = schedule.pop()
    if cost <= i:
        dp[i] = max(dp[i-cost] + value, dp[i-1])
    else:
        dp[i] = dp[i-1]
print(dp[-1])