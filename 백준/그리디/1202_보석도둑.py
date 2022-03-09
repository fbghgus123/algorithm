# 문제 : https://www.acmicpc.net/problem/1202
# 도움된 글 : https://velog.io/@piopiop/백준-1202-보석-도둑-Python

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []
bag = []
answer = 0

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewel, (m, v))
for _ in range(k):
    bag.append(int(input()))
bag.sort()

tmp = []
for i in bag:
    while jewel and jewel[0][0] <= i:
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jewel:
        break

print(answer)