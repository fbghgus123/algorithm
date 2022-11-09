# 문제 : https://www.acmicpc.net/problem/14719

h, w = map(int, input().split())
wall = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    height = min(max(wall[:i]), max(wall[i+1:]))
    answer += height - wall[i] if wall[i] < height else 0

print(answer)