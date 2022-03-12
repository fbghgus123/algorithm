import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

for _ in range(k):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1

def bfs(x, y):
    count = 1
    queue = deque()
    queue.append((x, y))
    grid[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0 <= cy < m and grid[cx][cy] == 1:
                queue.append((cx, cy))
                grid[x][y] = 0
                count += 1
    return count

maxx = 0 
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            tmp = bfs(i, j)
            if tmp > maxx:
                maxx = tmp
print(maxx)