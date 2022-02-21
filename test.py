import sys
import time
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

grid = [list(map(int, list(input().strip()))) for _ in range(n)]
grid[0][0] = 1

queue = deque()
queue.append((0, 0, 1))
while queue:
    # time.sleep(0.5)
    print(queue)
    now = queue.popleft()
    
    for i in range(4):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        if 0 <= x < n and 0 <= y < m:
            if grid[x][y] == 1 and now[2]:
                queue.append((x, y, 0))
            if grid[x][y] != 1 and (grid[x][y] == 0 or grid[x][y] > grid[now[0]][now[1]]):
                queue.append((x, y, now[2]))
                grid[x][y] = grid[now[0]][now[1]] + 1

if grid[n-1][m-1] == 0:
    print(-1)
else:
    print(grid[now[0]][now[1]]+1)

