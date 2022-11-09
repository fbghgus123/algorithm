# 문제: https://www.acmicpc.net/problem/2775

import sys
input = sys.stdin.readline

t = int(input())
apart = [[i for i in range(1, 15)]]

for _ in range(t):
    k = int(input())
    n = int(input())

    if len(apart)-1 < k:
        for i in range(len(apart), k+1):
            apart.append([])
            for j in range(14):
                apart[i].append(sum(apart[i-1][:j+1]))

    print(apart[k][n-1])