# 문제 : https://www.acmicpc.net/problem/2056

from collections import defaultdict, deque

n = int(input())
greed = [0]
cost = [0]
effect = defaultdict(list)

for i in range(1, n+1):
    t, c, *w = map(int, input().split())
    cost.append(t)
    greed.append(c)
    for need in w:
        effect[need].append(i)

time = [0] * (n+1)
queue = deque()
for i in range(1, n+1):
    if greed[i] == 0: queue.append(i)

while queue:
    now = queue.popleft()
    for i in effect[now]:
        greed[i] -= 1
        time[i] = max(time[i], time[now] + cost[now])
        if greed[i] == 0:
            queue.append(i)

answer = []
for i in range(1, n+1):
    answer.append(time[i] + cost[i])
print(max(answer))


