# 문제: https://www.acmicpc.net/problem/1759

import sys
import itertools
input = sys.stdin.readline

l, c = map(int, input().split())
spell = list(input().split())

j = []
m = []
answer = []

for i in spell:
    if i in ('a', 'e', 'i', 'o', 'u'):
        m.append(i)
    else:
        j.append(i)

for i in range(1, l-1):
    if len(m) < i or len(j) < l-i:
        continue
    mo = list(itertools.combinations(m, i))
    ja = list(itertools.combinations(j, l-i))

    for a in mo:
        for b in ja:
            answer.append(''.join(sorted(a+b)))
[print(i) for i in sorted(answer)]
    