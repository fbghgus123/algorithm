# 문제: https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
d = [1 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if p[i][0] > p[j][0] and p[i][1] > p[j][1]:
            d[j] += 1
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            d[i] += 1

print(' '.join(map(str,d)))