# 문제: https://www.acmicpc.net/problem/2631
# 도움된 글: https://ddiyeon.tistory.com/61

import sys
input = sys.stdin.readline

n = int(input())
line = [int(input()) for _ in range(n)]
dp = []

for i in line:
    dp.append(i)