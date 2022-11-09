# 문제: https://www.acmicpc.net/status?user_id=fbghgus123&problem_id=14501&from_mine=1

import sys
input = sys.stdin.readline

n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
dp = []

for i, v in enumerate(c):
    day = v[0]
    money = v[1]
    maxNum = (0, 0)

    for j in range(i):
        if dp[j] > maxNum[1] and c[j][0] <= i-j:
            maxNum = (j, dp[j])
    if i + day > n:
        dp.append(maxNum[1])
    else:
        dp.append(maxNum[1] + c[i][1])
    
print(max(dp))