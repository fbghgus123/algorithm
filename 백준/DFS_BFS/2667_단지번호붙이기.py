# 문제: https://www.acmicpc.net/problem/2667

from collections import deque
import queue

n = int(input())

mmap = []
visited = []
finded = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    mmap.append(list(map(int, list(input()))))
    visited.append([0 for _ in range(n)])

for i in range(n):
    for j in range(n):
        if mmap[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            queue = deque()
            queue.append((i,j))
            stack = [(i,j)]
            
            while queue:
                v = queue.popleft()
                
                for z in range(4):
                    x, y = v[0] + dx[z], v[1] + dy[z]

                    if x >= n or x < 0 or y >= n or y <0:
                        continue

                    if mmap[x][y] == 0:
                        continue

                    if visited[x][y] == 0:
                        visited[x][y] = 1
                        queue.append((x,y))
                        stack.append((x,y))
            finded.append(stack)

print(len(finded))
finded = sorted(finded, key = lambda x: len(x))
for i in finded:
    print(len(i))