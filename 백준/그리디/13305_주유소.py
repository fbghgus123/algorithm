# 문제: https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

n = int(input())
need = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()
oil = 0
minOil = 1_000_000_001

for i, v in enumerate(price):
    if v < minOil:
        minOil = v
    oil += minOil * need[i]

print(oil)
    