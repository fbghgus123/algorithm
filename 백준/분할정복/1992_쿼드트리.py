# 문제: https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

n = int(input())
video = [tuple(map(int, list(input().strip()))) for _ in range(n)]

def check(x, y, n, count=''):
    dn = n // 2
    all = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            all += video[i][j]

    if all == 0:
        return '0'
    if all == n**2:
        return '1'
    
    if n != 1:
        count += '('
        count += check(x, y, dn)
        count += check(x, y+dn, dn)
        count += check(x+dn, y, dn)
        count += check(x+dn, y+dn, dn)
        count += ')'
    return count

print(check(0, 0, n))