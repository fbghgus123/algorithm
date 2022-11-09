# 문제 : https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3

from collections import deque

# 1:우 2:하 3:좌 4:상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(board):
    h = len(board)
    w = len(board[0])
    
    cost = [[[0] * w for _ in range(h)] for _ in range(4)]
    # for i in range(4):
    #     cost[i][0][0] = 100
    queue = deque()
    queue.append((0, 0, -1))
    result = []
    while queue:
        y, x, d = queue.popleft()
        if y == h-1 and x == w-1:
            continue
        for i in range(4):
            cy = y + dy[i]
            cx = x + dx[i]
            if 0 <= cy < h and 0 <= cx < w:
                if board[cy][cx] == 1: continue
                # 직진
                if i == d or d == -1:
                    if cost[i][cy][cx] == 0 or cost[i][cy][cx] > cost[d][y][x] + 100:
                        cost[i][cy][cx] = cost[d][y][x] + 100
                        queue.append((cy, cx, i))
                # 꺾음
                else:
                    if cost[i][cy][cx] == 0 or cost[i][cy][cx] > cost[d][y][x] + 500:
                        cost[i][cy][cx] = cost[d][y][x] + 600
                        queue.append((cy, cx, i))
    # for i in range(4):
    #     [print(a) for a in cost[i]]
    #     print()
    return min([cost[i][h-1][w-1] for i in range(4) if cost[i][h-1][w-1] != 0])
    

def solution(board):
    return bfs(board)