# 문제: https://www.acmicpc.net/problem/3190

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

l = int(input())
turn = deque()
for _ in range(l):
    second, direction = input().rstrip().split()
    turn.append([int(second), direction])

snake = deque()
snake.append((0, 0))
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
second = 0

while(1):
    second += 1
    x, y = snake[-1]
    x += d[direction%4][1]
    y += d[direction%4][0]

    if 0 <= x < n and 0 <= y < n and (x, y) not in snake:
        snake.append((x, y))
    else:
        break 

    if board[y][x] == 1:
        board[y][x] = 0
    else:
        snake.popleft()

    if turn and turn[0][0] == second:
        turnD = turn.popleft()[1]

        if turnD == 'D':
            direction += 1
        else:
            direction -= 1
            if direction < 0: direction += 4

print(second)