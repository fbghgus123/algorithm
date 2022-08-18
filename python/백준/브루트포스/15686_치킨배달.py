# 문제: https://www.acmicpc.net/problem/15686
# 도움된 글 : https://juhee-maeng.tistory.com/96

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            home.append((i, j))
        elif grid[i][j] == 2:
            chicken.append((i, j))

minn = 99999
for ch in combinations(chicken, m):
    distance = 0
    for h in home:
        distance += min([abs(v[0] - h[0]) + abs(v[1] - h[1]) for v in ch])
    if distance < minn:
        minn = distance
print(minn)