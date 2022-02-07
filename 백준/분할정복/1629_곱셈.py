# 문제: https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def mul(a, b):
    if(b == 1):
        return a
    
    if b % 2 == 0:
        return mul(a, b//2) ** 2 % c
    else:
        return mul(a, b//2) ** 2 * mul(a, 1) %c

print(mul(a, b) % c)