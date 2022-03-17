# 문제 : https://www.acmicpc.net/problem/12851
# 도움된 글 : https://haerang94.tistory.com/74

from collections import deque

n, k = map(int, input().split())
dp = [-1] * 100_001
dp[n] = 0
count = 0

queue = deque()
queue.append(n)
while queue:
    n = queue.popleft()

    if k == n:
        count += 1

    if 0 <= n-1 <= 100_000 and (dp[n-1] == -1 or dp[n-1] == dp[n] + 1):
        dp[n-1] = dp[n] + 1
        queue.append(n-1)
    if 0 <= n*2 <= 100_000 and (dp[n*2] == -1 or dp[n*2] == dp[n] + 1):
        dp[n*2] = dp[n] + 1
        queue.append(n*2)
    if 0 <= n+1 <= 100_000 and (dp[n+1] == -1 or dp[n+1] == dp[n] + 1):
        dp[n+1] = dp[n] + 1
        queue.append(n+1)

print(dp[k])
print(count)
