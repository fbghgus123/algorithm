# 문제: https://www.acmicpc.net/problem/2309

import sys
import itertools
input = sys.stdin.readline

n = [int(input()) for _ in range(9)]
n.sort()
c = list(itertools.combinations(n, 7))

for i in c:
    if sum(i) == 100:
        answer = i
        break

[print(i) for i in answer]