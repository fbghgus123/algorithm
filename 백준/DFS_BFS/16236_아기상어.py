# 문제 : https://www.acmicpc.net/problem/16236

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
big = count = 2

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            y, x = i, j
            break

def search(y, x):
    visited = [[0] * n for _ in range(n)]
    searched = []
    minn = n**2
    queue = deque()
    queue.append((y, x, 0))
    visited[y][x] = 1

    while queue:
        now = queue.popleft()
        if grid[now[0]][now[1]] != 0 and big > grid[now[0]][now[1]] and visited[now[0]][now[1]] == 0:
            searched.append(now)
            minn = now[2]
            visited[now[0]][now[1]] = 1
            continue
        visited[now[0]][now[1]] = 1
        for i in range(4):
            cx = now[1] + dx[i]
            cy = now[0] + dy[i]
            if 0 <= cx < n and 0 <= cy < n and visited[cy][cx] == 0:
                if big >= grid[cy][cx] and minn >= now[2]+1:
                    queue.append((cy, cx, now[2]+1))
    print(visited)
    return sorted(searched, key=lambda x : (x[2], x[0], x[1]))

answer = 0
while(1):
    searched = search(y,x)
    if searched:
        grid[y][x] = 0
        y, x, length = searched[0]
        answer += length
        count -= 1
        if count == 0:
            big += 1
            count = big
    else:
        break
print(answer)