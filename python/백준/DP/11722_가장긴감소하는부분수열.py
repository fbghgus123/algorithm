# 문제 : https://www.acmicpc.net/problem/11722

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[i] for i in nums]

for i in range(n):
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            dp[j] = dp[i] + [nums[j]] if len(dp[i] + [nums[j]]) > len(dp[j]) else dp[j]
print(len(sorted(dp, key = lambda x : len(x))[-1]))