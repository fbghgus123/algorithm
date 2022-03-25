import sys
import copy
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt():
    global grid
    tmp = copy.deepcopy(grid)
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'X':
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c and grid[x][y] == '.':
                        tmp[i][j] = '.'
                        break
    grid = tmp

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < r and 0 <= cy < c and grid[cx][cy] != 'X' and visited[cx][cy] == 0:
                visited[cx][cy] = 1
                queue.append((cx, cy))
    return visited

count = -1
while(1):
    count += 1
    flag1 = False
    flag2 = False
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'L':
                if not flag1:
                    visited = bfs(i, j)
                    flag1 = True
                elif visited[i][j] == 0: 
                    flag2 = True
                    break
        if flag2: break
    if flag2 == False: break
    melt()
print(count)