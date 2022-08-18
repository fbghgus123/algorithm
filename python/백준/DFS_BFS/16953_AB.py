# 문제 : https://www.acmicpc.net/problem/16953

import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int,input().split())

queue = deque()
queue.append((a, 1))
flag = True
while queue:
    num, count = queue.popleft()
    if num == b:
        print(count)
        flag = False
        break

    if num * 2 <= b:
        queue.append((num*2, count + 1))

    tmp = int(str(num) + '1')
    if tmp <= b:
        queue.append((tmp, count + 1))

if flag:
    print(-1)