import sys
import heapq
input = sys.stdin.readline
n = int(input())
lecture = []
for _ in range(n):
    p, d = map(int, input().split())
    lecture.append([p, d])
lecture = sorted(lecture, key=lambda x:x[1])

queue = []
for p, d in lecture:
    heapq.heappush(queue, p)
    if len(queue) > d:
        heapq.heappop(queue)
print(sum(queue))
