# 문제: https://www.acmicpc.net/problem/1463

from collections import deque
n = int(input())

visited = [0 for _ in range(n+1)]
queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x==1:
        print(visited[x])
        break
    if x%3==0 and visited[x//3] == 0:
        visited[x//3] = visited[x] + 1
        queue.append(x//3)
    if x%2==0 and x > 1 and visited[x//2] == 0:
        visited[x//2] = visited[x] + 1
        queue.append(x//2)
    if x>1 and visited[x-1] == 0:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)