# 문제 : https://www.acmicpc.net/problem/2638

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    global cheese
    tmp = [[-1] * m for _ in range(n)]
    tmp[0][0] = 0

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if tmp[x][y] == 0:
                    if tmp[cx][cy] == -1: 
                        tmp[cx][cy] = 0
                        queue.append((cx, cy))
                    if cheese[cx][cy] >= 1:
                        if tmp[cx][cy] == -1: tmp[cx][cy] = 1
                        else: tmp[cx][cy] += 1
    for i in range(n):
        for j in range(m):
            if tmp[i][j] > 1:
                cheese[i][j] = 0

def check():
    global n, m, cheese
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                return True
    return False

flag = check()
count = 0
while flag:
    bfs()
    flag = check()
    count += 1
print(count)