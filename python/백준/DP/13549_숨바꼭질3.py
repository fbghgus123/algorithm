# 문제 : https://www.acmicpc.net/problem/13549
# 도움된 글 : https://tooo1.tistory.com/462

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [-1] * 100_001

queue = deque()
queue.append(n)
dp[n] = 0
while queue:
    n = queue.popleft()
    if 0 <= n-1 < 100_001 and dp[n-1]==-1:
        dp[n-1] = dp[n] + 1
        if n - 1 == k: break
        queue.append(n-1)
    if 0 <= n*2 < 100_001 and dp[n*2]==-1:
        dp[n*2] = dp[n]
        if n * 2 == k: break
        queue.append(n*2)
    if 0 <= n+1 < 100_001 and dp[n+1]==-1:
        dp[n+1] = dp[n] + 1
        if n + 1 == k: break
        queue.append(n+1)
    
print(dp[k])