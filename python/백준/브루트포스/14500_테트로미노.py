# 문제 : https://www.acmicpc.net/problem/14500

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check(x, y):
    select = []
    queue = []
    visited = []
    heapq.heappush(queue, (-grid[x][y], x, y))
    
    for _ in range(4):
        if queue:
            now = heapq.heappop(queue)
            visited.append((now[1], now[2]))
            select.append(grid[now[1]][now[2]])
        else:
            return 0
        for i in range(4):
            cx = now[1] + dx[i]
            cy = now[2] + dy[i]
            if 0 <= cx < n and 0 <= cy < m and (cx, cy) not in visited:
                heapq.heappush(queue, (-grid[cx][cy], cx, cy))
    return sum(select)

maxx = 0
for i in range(n):
    for j in range(m):
        tmp = check(i, j)
        if maxx < tmp:
            maxx = tmp
print(maxx)