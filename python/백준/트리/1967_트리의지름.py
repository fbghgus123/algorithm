import sys
sys.setrecursionlimit(100000)
# 문제 : https://www.acmicpc.net/problem/1967

input = sys.stdin.readline


n = int(input())
path = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, c = map(int, input().split())
    path[s].append((e, c))
    path[e].append((s, c))

maxx = [0, 0]
def dfs(prev, n, cost):
    global maxx
    if maxx[0] < cost: maxx = [cost, n]

    for d, c in path[n]:
        if d == prev: continue
        dfs(n, d, cost + c)

dfs(0, 1, 0)
dfs(0, maxx[1], 0)
print(maxx[0])