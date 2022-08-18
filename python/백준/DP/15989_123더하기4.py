# 문제 : https://www.acmicpc.net/problem/15989
# 도움된 글 : https://velog.io/@dhelee/백준-15989번-123-더하기-4-Python-다이나믹-프로그래밍DP

t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])