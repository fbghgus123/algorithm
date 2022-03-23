# 문제 : https://www.acmicpc.net/problem/1826

import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
nums = deque(sorted(nums, key=lambda x : x[0]))
l, p = map(int, input().split())

answer = 0
queue = []
flag = False

while nums or queue:
    if p >= l:
        flag = True
        break

    if nums and nums[0][0] <= p:
        a, b = nums.popleft()
        heapq.heappush(queue, -b)

    elif queue:
        answer += 1
        p -= heapq.heappop(queue)

    else:
        break 

if flag: print(answer)
else: print(-1)