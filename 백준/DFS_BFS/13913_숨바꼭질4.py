# 문제 : https://www.acmicpc.net/problem/13913

from collections import deque
import sys
sys.setrecursionlimit(100000)

s, k = map(int, input().split())
dp = [-1] * 100_001
trace = [-1] * 100_001
dp[s] = 0

queue = deque()
queue.append(s)

while queue:
    n = queue.popleft()
    if 0 <= n - 1 and dp[n-1] == -1: 
        queue.append(n-1)
        dp[n-1] = dp[n] + 1
        trace[n-1] = n
        if n-1 == k: break
    if n * 2 <= 100_000 and dp[n*2] == -1:
        queue.append(n*2)
        dp[n*2] = dp[n] + 1
        trace[n*2] = n
        if n*2 == k: break
    if n + 1 <= 100_000 and dp[n+1] == -1: 
        queue.append(n+1)
        dp[n+1] = dp[n] + 1
        trace[n+1] = n
        if n+1 == k: break

answer = []
x = k

while trace[x] != -1:
    answer.append(x)
    x = trace[x]
answer += [s]
print(dp[k])
print(*answer[::-1])