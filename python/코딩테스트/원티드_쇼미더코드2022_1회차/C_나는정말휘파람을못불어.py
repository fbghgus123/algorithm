# 정답 코드
maxx = 1_000_000_007
n = int(input())
string = input()

dp = [0] * n
countE = [0] * n
count = [0, 0, 0]

answer = 0
for i in range(n):
    if string[i] == 'W':
        count[0] += 1
    if string[i] == 'H':
        count[1] += count[0]
    if string[i] == 'E':
        dp[i] = count[1]
        answer += answer
        answer += count[2]
        answer %= maxx
        count[2] += count[1]
print(answer % maxx)
