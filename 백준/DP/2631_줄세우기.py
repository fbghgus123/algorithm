# 문제: https://www.acmicpc.net/problem/2631
# 도움된 글: https://ddiyeon.tistory.com/61

import sys
input = sys.stdin.readline

N = int(input())
dp = [(0, 0)]*(N+1)
print(dp)
_max = 0
for i in range(1, N+1):
    n = int(input())
    for j in range(i):
        if dp[j][0]<n :
            dp[i] = (n, max(dp[j][1]+1, dp[i][1]))
            _max = max(_max, dp[i][1])
print(N-_max)