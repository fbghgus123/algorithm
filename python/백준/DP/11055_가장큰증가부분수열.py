# 문제 : https://www.acmicpc.net/problem/11055

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = nums.copy()

for i in range(n):
    for j in range(i+1, n):
        if nums[i] < nums[j]:
            dp[j] = max(dp[i] + nums[j], dp[j])
print(max(dp))