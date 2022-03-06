# 문제 : https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

l, r = 0, max(tree)
flag = True
while l <= r:
    mid = (l + r) // 2
    revenue = 0
    for i in tree:
        revenue += i - mid if i >= mid else 0

    if revenue == m:
        break
    elif revenue > m:
        l = mid + 1
    else:
        r = mid - 1

revenue = 0
for i in tree:
    revenue += i - mid if i >= mid else 0 

if revenue < m: print(mid - 1)
else: print(mid)