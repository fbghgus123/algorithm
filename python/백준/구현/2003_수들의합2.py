# 문제: https://www.acmicpc.net/problem/2003

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

p1 = 0
p2 = 1

while(p1 < p2 <= n):
    amount = sum(a[p1:p2])
    if amount == m:
        p2 += 1
        answer += 1
    elif amount < m or len(a[p1:p2]) == 1:
        p2 += 1
    else:
        p1 += 1

print(answer)


