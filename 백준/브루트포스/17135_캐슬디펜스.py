# 문제 : https://www.acmicpc.net/problem/17135

import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

n, m, d = map(int, input().split())
dx = 0, -1, 0
dy = -1, 0, 1
enemy = [list(map(int, input().split())) for _ in range(n)]

def find(x, y, d):
    queue = deque()
    queue.append((x, y, d))
    while queue:
        x, y, d = queue.popleft()
        if enemy_tmp[x][y] == 1:
            return x, y
        if d > 0:
            for i in range(3):
                cx = x + dx[i]
                cy = y + dy[i]
                if 0 <= cx < n and 0 <= cy < m:
                    queue.append((cx, cy, d-1))
    return -1, -1

def defence(archor):
    summ = 0
    tmp = [[0] * m for _ in range(n)]
    for row in range(n-1, -1, -1):
        delete = set()
        for i in archor:
            x, y = find(row, i, d-1)
            if x != -1 and tmp[x][y] == 0:
                tmp[x][y] = 1
                delete |= {(x, y)}
        for x, y in list(delete):
            enemy_tmp[x][y] = 0
    for i in tmp:
        summ += sum(i)
    return summ

maxx = []
for i in combinations(range(m), 3):
    enemy_tmp = copy.deepcopy(enemy)
    maxx.append(defence(i))
print(max(maxx))