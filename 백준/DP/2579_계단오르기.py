# 문제: https://www.acmicpc.net/problem/2579
# 도움된 글: https://sungmin-joo.tistory.com/18

import sys
input = sys.stdin.readline

l = int(input())
arr = [int(input()) for _ in range(l)]

dp = [arr[0]]
if l > 1:
    dp.append(max(arr[0]+arr[1], arr[1]))
if l > 2:
    dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
    for i in range(3, l):
        dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1]))

print(dp.pop())


