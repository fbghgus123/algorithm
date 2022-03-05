n = int(input())
num = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if num[i] < num[j]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][i] + 1)
        else:
            dp[i][j] = dp[i-1][j]

[print(i) for i in dp]