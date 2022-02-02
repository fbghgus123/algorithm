# 문제: https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0

def checkPaper(x, y, n):
    global white, blue
    all = 0
    dn = n // 2
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            all += paper[i][j]

    if all == 0:
        white += 1
        return

    if all == n**2:
        blue += 1
        return
    if n != 1:
        checkPaper(x, y, dn)
        checkPaper(x+dn, y, dn)
        checkPaper(x, y+dn, dn)
        checkPaper(x+dn, y+dn, dn)

checkPaper(0, 0, n)
print(white)
print(blue)
