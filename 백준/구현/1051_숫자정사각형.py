# 문제 : https://www.acmicpc.net/problem/1051

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maxx = min(n, m)
minn = 0

nums = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        for e in range(minn+1, maxx):
            if 0 <= i+e < n and 0 <= j+e < m:
                if nums[i][j] == nums[i][j+e] and nums[i][j] == nums[i+e][j] and nums[i][j] == nums[i+e][j+e]:
                    minn = e
            else: break

print((minn+1) ** 2)
