# 문제: https://www.acmicpc.net/problem/1263

import sys
input = sys.stdin.readline

n = int(input())
work = [tuple(map(int, input().split())) for _ in range(n)]

work = sorted(work, key=lambda x : x[1], reverse = True)
current = 1_000_000
for i in work:
    if current > i[1]:
        current = i[1]
    current -= i[0]

    if current < 0:
        current = -1
        break

print(current)