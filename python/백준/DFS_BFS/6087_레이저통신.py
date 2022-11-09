# 문제 : https://www.acmicpc.net/problem/6087

from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(m)]
visited = [[[-1] * n for _ in range(m)] for _ in range(4)]

c = []

for ri, row in enumerate(grid):
    for ci, v in enumerate(row):
        if v == 'C':
            c.append((ri, ci))
# 하 우 상 좌
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def bfs():
    queue = deque()
    for i in range(4):
        visited[i][c[0][0]][c[0][1]] = 0
        queue.append((*c[0], i))
    while queue:
        y, x, prev = queue.popleft()
        for i in range(4):
            cy = y + dy[i]
            cx = x + dx[i]
            if 0 <= cy < m and 0 <= cx < n:
                if grid[cy][cx] != '*':
                    if i == prev and (visited[i][cy][cx] == -1 or visited[i][cy][cx] > visited[i][y][x]):
                        visited[i][cy][cx] = visited[i][y][x]
                        queue.append((cy, cx, i))
                    if i != prev and (visited[i][cy][cx] == -1 or visited[i][cy][cx] > visited[prev][y][x] + 1):
                        visited[i][cy][cx] = visited[prev][y][x] + 1
                        queue.append((cy, cx, i))

bfs()
minn = 100000
for i in range(4):
    if visited[i][c[1][0]][c[1][1]] == -1: continue
    minn = min(minn, visited[i][c[1][0]][c[1][1]])
print(minn)