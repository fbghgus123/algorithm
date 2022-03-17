import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    for i in range(n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + sticker[1][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + sticker[0][i])
    
    maxx = 0
    for i in dp:
        maxx = max(maxx, max(i))
    print(maxx)