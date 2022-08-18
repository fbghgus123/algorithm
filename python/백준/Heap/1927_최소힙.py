# 문제 : https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    tmp = int(input())
    if tmp:
        heapq.heappush(heap, tmp)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
