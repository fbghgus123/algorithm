# 문제 : https://www.acmicpc.net/problem/1005

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    degree = [0] * (n+1)
    rule = [[] for _ in range(n+1)]
    for _ in range(k):
        s, e = map(int, input().split())
        rule[s].append(e)
        degree[e] += 1

    queue = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            queue.append(i)
    m = [0] * (n+1)
    while queue:
        v = queue.popleft()
        for i in rule[v]:
            if m[i] < m[v] + time[v-1]:
                m[i] = m[v] + time[v-1]
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)
    answer = int(input())
    print(m[answer] + time[answer-1])

