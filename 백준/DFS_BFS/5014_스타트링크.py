# 문제: https://www.acmicpc.net/problem/5014

from collections import deque
f, s, g, u, d = map(int, input().split())

building = [-1 for _ in range(f+1)]

queue = deque()
queue.append(s)
building[s] = 0

def bfs():
    if (g > s and u == 0) or (g < s and d == 0):
        return "use the stairs"

    while queue:
        c = queue.popleft()
        if c == g: return building[c]
        if c + u <=f and building[c+u] == -1 and u != 0:
            building[c+u] = building[c] + 1
            queue.append(c+u)
        if 0 < c - d and building[c-d] == -1 and d != 0:
            building[c-d] = building[c] + 1
            queue.append(c-d)
    return "use the stairs"

print(bfs())



