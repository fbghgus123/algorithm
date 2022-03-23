# 문제 : https://www.acmicpc.net/problem/16235

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [[5] * n for _ in range(n)]
initial = [list(map(int, input().split())) for _ in range(n)]
trees = defaultdict(list)
dead = []
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[z].append((x-1, y-1))

def spring():
    global trees, a, dead
    tmp = defaultdict(list)
    for i, tree in trees.items():
        for x, y in tree:
            if a[x][y] >= i:
                a[x][y] -= i
                tmp[i+1].append((x, y))
            else:
                dead.append((x, y, i//2))
    trees = tmp

def summer():
    global a, dead
    for x, y, c in dead:
        a[x][y] += c

def autumn():
    global trees, a
    tmp = defaultdict(list)
    for i, tree in trees.items():
        tmp[i] += tree
        if i % 5 == 0:
            for x, y in tree:
                if i % 5 == 0:
                    for dx, dy in d:
                        cx = x + dx
                        cy = y + dy
                        if 0 <= cx < n and 0 <= cy < n:
                            tmp[1].append((cx, cy))
    trees = tmp

def winter():
    global a, initial
    for i in range(n):
        for j in range(n):
            a[i][j] += initial[i][j]

for _ in range(k):
    spring()
    summer()
    autumn()
    winter()

summ = 0
for i in trees.values():
    summ += len(i)
print(summ)