# 문제: https://www.acmicpc.net/problem/2302
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

nums = []
count = 1
start = 1

dp = [1, 1, 2]
for i in range(3, 41):
    dp.append(dp[i-1] + dp[i-2])

if m > 0:
    for i in range(m):
        num = int(input())
        count *= dp[num-start]
        start = num + 1
    count *= n - start + 1
    print(count)
else:
    print(dp[n])