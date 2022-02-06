# 문제: https://www.acmicpc.net/problem/9205

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
answer = []

def bfs(v):
    visited = [v]
    queue = deque()
    queue.append(v)

    while(queue):
        v = queue.popleft()
        for i in goFestival:
            if i not in visited and abs(i[0]-v[0]) + abs(i[1]-v[1]) <= 1000:
                visited.append(i)
                queue.append(i)
    return visited

for _ in range(t):
    n = int(input())
    goFestival = [list(map(int, input().split())) for _ in range(n+2)]
    if goFestival[-1] in bfs(goFestival[0]):
        answer.append("happy")
    else:
        answer.append("sad")

[print(ans) for ans in answer]