# 문제: https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

n = int(input())
region = list(map(int, input().split()))
m = int(input())

tmp = 0

def check(region, m):
    a = m // len(region)
    tmp = []
    for i in region:
        if a > i:
            m -= i
        else:
            tmp.append(i)
    if len(region) == len(tmp) or len(tmp) == 0:
        return tmp, m
    return check(tmp, m)

region2, m = check(region, m)
if len(region2) == 0:
    print(max(region))
else:
    print(m//len(region2))