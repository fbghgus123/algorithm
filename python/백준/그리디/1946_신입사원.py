# 문제 : https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score = sorted(score, key=lambda x : x[0])
    maxx = n+1
    count = 0
    for i in score:
        if maxx > i[1]:
            count += 1
            maxx = i[1]
    print(count)