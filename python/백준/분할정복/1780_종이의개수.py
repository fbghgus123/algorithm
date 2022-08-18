# 문제: https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

one = 0
zero = 0
minus = 0

def check(x, y, n):
    global one, zero, minus
    dn = n // 3
    all = 0
    start = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if start != paper[i][j]: start = 2
            all += paper[i][j]

    if all == 0 and start != 2:
        zero += 1
        return
    if all == n**2:
        one += 1
        return
    if all == -n**2:
        minus += 1
        return

    for i in range(3):
        for j in range(3):
            dx = x + dn*i
            dy = y + dn*j
            check(dx, dy, dn)
check(0, 0, n)
print(minus)
print(zero)
print(one)
    
