import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lamp = [list(input().strip()) for _ in range(n)]
k = int(input())
chance = k

for _ in range(k):
    light = [0] * m
    for i in range(n):
        if lamp[i].count('0') % 2 == chance % 2 and lamp[i].count('0') < k:
            for j in range(m):
                if lamp[i][j] == '0':
                    light[j] += 1    
    chance -= 1
    idx = light.index(max(light))

    for i in range(n):
        lamp[i][idx] = '0' if lamp[i][idx] == '1' else '1'

answer = 0
for i in lamp:
    if sum(map(int, i)) == m:
        answer += 1

print(answer)