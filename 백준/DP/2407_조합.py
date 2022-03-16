# 문제 : https://www.acmicpc.net/problem/2407

dp = [0] * 101
dp[1] = 1

def factorial(n):
    if dp[n]:
        return dp[n]
    else:
        dp[n] = factorial(n-1) * n
        return dp[n]

n, m = map(int, input().split())
print(factorial(n) // (factorial(n-m) * factorial(m)))
