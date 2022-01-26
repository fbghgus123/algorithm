# 문제: https://www.acmicpc.net/problem/1697
# 도움된 글: https://tooo1.tistory.com/111

from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        if v == k:
            return dist[v]
        dx = [v-1, v+1, v*2]
        for i in dx:
            if 0 <= i <= MAX and not dist[i]:        
                dist[i] = dist[v] + 1
                queue.append(i)
MAX = 10 ** 5
n, k = map(int, input().split())
dist = [0] * (MAX+1)
print(bfs(n))