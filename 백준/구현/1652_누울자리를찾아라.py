# 문제: https://www.acmicpc.net/problem/1652

import sys
input = sys.stdin.readline

n = int(input())
room = [input() for i in range(n)]
a = b = 0

for i in range(n):
    flag1 = flag2 = True
    for j in range(n):
        if j < n-1:
            if flag1 and room[i][j] == '.' and room[i][j+1] == '.':
                a += 1
                flag1 = False
            elif room[i][j] == 'X':
                flag1 = True
            if flag2 and room[j][i] == '.' and room[j+1][i] == '.':
                b += 1
                flag2 = False
            elif room[j][i] == 'X':
                flag2 = True
print(a, b)
