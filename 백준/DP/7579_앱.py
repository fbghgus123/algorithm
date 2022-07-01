# 문제 : https://www.acmicpc.net/problem/7579
# 도움된 글 : https://velog.io/@uoayop/BOJ-7579-앱Python

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

total =  sum(c)
dp = [[0] * (total+1) for _ in range(n+1)]

def check():
    for j in range(total+1):
        for i in range(1, n+1):
            memory = a[i-1]
            time = c[i-1]
            if j >= time:
                dp[i][j] = max(dp[i-1][j-time]+memory, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

            if dp[i][j] >= m:
                return j

print(check())