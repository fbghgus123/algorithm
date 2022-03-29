n, m = map(int, input().split())
a = map(int, input().split())
c = list(map(int, input().split()))

summ = sum(c.copy())
app = list(zip(a, c))
app.insert(0, (0, 0))

dp = [[0] * (n+1) for _ in range(summ+1)]

for i in range(1, summ+1):
    for j in range(1, len(app)+1):
        memory, cost = app[j]
        if cost >= i:
            dp[i][j] = max(dp[i-cost][j] + memory, dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

[print(i) for i in dp]