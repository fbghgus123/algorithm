# 문제 : https://www.acmicpc.net/problem/11279

import sys
import heapq
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    tmp = int(input())
    if tmp:
        heapq.heappush(num, -tmp)
    else:
        if num:
            print(-heapq.heappop(num))
        else:
            print(0)