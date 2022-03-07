# 문제 : https://www.acmicpc.net/problem/14466

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, k, r = map(int, input().split())
cow = [[0] * (n+1) for _ in range(n+1)]
path = [[[] for _ in range(n+1)] for _ in range(n+1)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = []

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    mover = r2 - r1
    movec = c2 - c1
    direction_num = direction.index((mover, movec))
    path[r1][c1].append(direction_num)
    if direction_num % 2 == 0:
        path[r2][c2].append(direction_num + 1)
    else:
        path[r2][c2].append(direction_num - 1)

for _ in range(k):
    r, c = map(int, input().split())
    cow[r][c] = 1

def bfs(x, y):
    count = 0
    if cow[x][y] == 1: count += 1
    cow[x][y] = -1

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if i in path[x][y]: continue
            cx = x + direction[i][0]
            cy = y + direction[i][1]
            if 0 < cx <= n and 0 < cy <= n and cow[cx][cy] != -1:
                if cow[cx][cy] == 1: count += 1
                cow[cx][cy] = -1
                queue.append((cx, cy))
    if count > 0: answer.append(count)

for i in range(1, n+1):
    for j in range(1, n+1):
        if cow[i][j] != -1:
            bfs(i, j)

couple = 0
if len(answer) > 1:
    while answer:
        couple += answer.pop() * sum(answer)
print(couple)