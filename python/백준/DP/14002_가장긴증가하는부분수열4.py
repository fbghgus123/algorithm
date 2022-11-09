# 문제 : https://www.acmicpc.net/problem/14002

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * (n+1)
trace = [0] * (n+1)
maxx = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        if nums[i-1] < nums[j-1]:
            if dp[j] < dp[i] + 1:
                dp[j] = dp[i] + 1
                trace[j] = i

        if dp[maxx] < dp[j]:
            maxx = j

answer = []
while trace[maxx] != 0:
    answer.append(nums[maxx-1])
    maxx = trace[maxx]
answer.append(nums[maxx-1])

print(max(dp))
print(*answer[::-1])