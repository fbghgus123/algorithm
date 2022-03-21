# 문제 : https://www.acmicpc.net/problem/11725

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

n = int(input())
path = [[] for _ in range(n+1)]
parent = [0] * (n+1)
parent[1] = 1

for _ in range(n-1):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

def dfs(n):
    for i in path[n]:
        if parent[i] == 0:
            parent[i] = n
            dfs(i)
dfs(1)            
[print(i) for i in parent[2:]]