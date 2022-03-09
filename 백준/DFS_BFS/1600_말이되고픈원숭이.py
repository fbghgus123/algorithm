# 문제 : https://www.acmicpc.net/problem/1600

import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

dp = [[[0] * w for _ in range(h)] for _ in range(k+1)]

move = [(0, 0, 1), (0, 1, 0), (0, -1, 0), (0, 0, -1)]
horse_move = [(-1, -1, -2), (-1, -2, -1), (-1, -2, 1), (-1, -1, 2), (-1, 1, -2), (-1, 2, -1), (-1, 1, 2), (-1, 2, 1)]

queue = deque()
queue.append((k, 0, 0))
dp[k][0][0] = 1

while queue:
    k, x, y = queue.popleft()
    if k > 0:
        for i in range(8):
            ck = k - 1
            cx = x + horse_move[i][1]
            cy = y + horse_move[i][2]
            if 0 <= cx < h and 0 <= cy < w and grid[cx][cy] != 1 and dp[ck][cx][cy] == 0:
                queue.append((ck, cx, cy))
                dp[ck][cx][cy] = dp[k][x][y] + 1
    for i in range(4):
        cx = x + move[i][1]
        cy = y + move[i][2]
        if 0 <= cx < h and 0 <= cy < w and grid[cx][cy] != 1 and dp[k][cx][cy] == 0:
            queue.append((k, cx, cy))
            dp[k][cx][cy] = dp[k][x][y] + 1

minn = 200 ** 2
for i in dp:
    if i[h-1][w-1] < minn and i[h-1][w-1] != 0:
        minn = i[h-1][w-1]
if minn == 200 ** 2:
    print(-1)
else:
    print(minn - 1)
