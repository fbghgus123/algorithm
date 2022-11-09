# 문제 : https://www.acmicpc.net/problem/14891

import sys
from collections import deque
input = sys.stdin.readline

option = []
for _ in range(4):
    option.append(deque(input().strip()))

def cal():
    tmp = [[0, 0] for _ in range(4)]
    for i in range(4):
        if i < 3 and option[i][2] != option[i+1][-2]:
            tmp[i][1] = 1
        if i > 0 and option[i][-2] != option[i-1][2]:
            tmp[i][0] = 1
    return tmp

def rotate(num, direction):
    if direction == 1:
        option[num-1].appendleft(option[num-1].pop())
    else:
        option[num-1].append(option[num-1].popleft())

k = int(input())
for _ in range(k):
    connect = cal()
    visited = [0, 0, 0, 0]
    queue = deque()
    num, direction = map(int, input().split())
    queue.append((num, direction))

    while queue:
        num, direction = queue.popleft()
        rotate(num, direction)
        visited[num-1] = 1
        if num - 1 > 0 and connect[num-1][0] == 1 and visited[num-2] == 0:
            queue.append((num-1, -direction))
        if num < 4 and connect[num-1][1] == 1 and visited[num] == 0:
            queue.append((num+1, -direction))

ans = 0
for i in range(4):
    ans += 2 ** i * int(option[i][0])
print(ans)