# 문제 : https://www.acmicpc.net/problem/15591

import sys
from collections import deque, defaultdict
input = sys.stdin.readline
INF = sys.maxsize

N, Q = map(int, input().split())
dp = defaultdict(list)
for _ in range(N-1):
    p, q, r = map(int, input().split())
    dp[p].append((q, r))
    dp[q].append((p, r))

def bfs(start, k):
    queue = deque()
    queue.append((start, INF))
    distance = [0] * (N+1)
    distance[start] = -1
    while queue:
        now, minn = queue.popleft()
        for i in dp[now]:
            if distance[i[0]] == 0:
                tmp = i[1] if minn > i[1] else minn
                distance[i[0]] = tmp
                queue.append((i[0], tmp))

    return len(list(filter(lambda x : x >= k, distance)))

for _ in range(Q):
    k, s = map(int, input().split())
    print(bfs(s, k))

