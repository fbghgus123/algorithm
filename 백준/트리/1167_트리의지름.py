# 문제 : https://www.acmicpc.net/problem/1167
# 도움된 글 : https://tsgoing.tistory.com/28

from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
maxx = 0
z = 0

for _ in range(n):
    path = deque(map(int, input().split()))
    node = path.popleft()
    while True:
        c = path.popleft()
        if c == -1: break
        distance = path.popleft()
        tree[node].append((c, distance))

def dfs(prev, node, summ):
    global maxx
    global z
    if maxx < summ: 
        maxx = summ
        z = node

    for i in tree[node]:
        if i[0] == prev: continue
        dfs(node, i[0], summ + i[1])

dfs(0, 1, 0)
dfs(0, z, 0)

print(maxx)