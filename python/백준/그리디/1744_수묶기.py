# 문제 : https://www.acmicpc.net/problem/1744

import sys
import heapq
input = sys.stdin.readline

plus = []
minus = []
ect = 0
answer = 0

n = int(input())
for _ in range(n):
    num = int(input())
    if num == 1:
        ect += 1
    elif num > 1:
        heapq.heappush(plus, -num)
    else:
        heapq.heappush(minus, num)

while len(plus) > 1:
    num1 = heapq.heappop(plus)
    num2 = heapq.heappop(plus)
    answer += num1 * num2

while len(minus) > 1:
    num1 = heapq.heappop(minus)
    num2 = heapq.heappop(minus)
    answer += num1 * num2

plus = list(map(lambda x : -x, plus))
answer += sum(plus + minus + [ect])
print(answer)