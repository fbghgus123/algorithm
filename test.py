N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().split())))

lineList.sort()

dp = [1]*N
for i in range(N):
    print(dp)
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
            print(i, j)

print(N-max(dp))