import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
computers = dict()
maxx = 0

for i in range(m):
    b, a = map(int, input().split())
    if a in computers:
        computers[a].append(b)
    else:
        computers[a] = [b]

def bfs(v):
    check = [0] * (n+1)
    queue = deque()
    queue.append(v)
    check[v] = 1
    while queue:
        v = queue.popleft()
        if v in computers:
            for i in computers[v]:
                if check[i] == 0:
                    check[v] = 1
                    queue.append(i)
    return sum(check)

answer = []
for i in range(1, n+1):
    count = bfs(i)
    if count > maxx:
        answer = [i]
        maxx = count
    elif count == maxx:
        answer.append(i)
print(*answer)