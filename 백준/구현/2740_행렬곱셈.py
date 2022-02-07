# 문제: https://www.acmicpc.net/problem/2740

import sys
input = sys.stdin.readline

an, am = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(an)]

bn, bm = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(bn)]

answer = []

for i in range(an):
    for j in range(bm):
        tmp = 0
        for c in range(am):
            tmp += a[i][c] * b[c][j]
        answer.append(tmp)
[print(*answer[i*bm:i*bm+bm]) for i in range(an)]