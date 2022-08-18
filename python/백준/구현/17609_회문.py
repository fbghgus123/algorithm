# 문제: https://www.acmicpc.net/problem/17609

import sys
from collections import deque
input = sys.stdin.readline

answer = []
t = int(input())

def isPalin(string):
    return string == string[::-1]

for _ in range(t):
    n = input().strip()
    string = deque()
    [string.append(a) for a in n]

    if n == n[::-1]:
        answer.append(0)
        continue

    while(len(string) > 1):
        a = string.popleft()
        b = string.pop()
        if a != b:
            tmp = list(string)
            if isPalin([a]+tmp) or isPalin(tmp+[b]):
                answer.append(1)
                break
            else:
                answer.append(2)
                break
[print(i) for i in answer]