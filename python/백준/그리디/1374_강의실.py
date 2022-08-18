# 문제: https://www.acmicpc.net/problem/1374

import sys
import heapq
input = sys.stdin.readline

heap = []
room = []

n = int(input())
for _ in range(n):
    num, start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(heap, [start,end,num])

start, end, num = heapq.heappop(heap)
heapq.heappush(room, end)

while heap:
    start, end, num = heapq.heappop(heap)
    if room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))