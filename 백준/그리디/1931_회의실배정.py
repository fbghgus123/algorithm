# 문제: https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for i in range(n)]
times = sorted(times, key = lambda time: (time[1], time[0]))

endTime = 0
answer = 0
for time in times:
    if time[0] >= endTime:
        answer += 1
        endTime = time[1]

print(answer)