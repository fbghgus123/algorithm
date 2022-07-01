# 정답 코드

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, q = map(int, input().split())
nums = input().strip().split()

path = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    path[s].append(e)
    path[e].append(s)

def dfs(prev, n):
    global trace
    trace[n] = prev
    for i in path[n]:
        if i == prev: continue
        dfs(n, i)

for _ in range(q):
    answer = []
    trace = [0] * (n+1)
    s, e = map(int, input().split())
    dfs(0, s)
    
    while trace[e] != 0:
        answer.append(nums[e-1])
        e = trace[e]
    answer.append(nums[e-1])

    print(int(''.join(answer[::-1])) % 1_000_000_007)
