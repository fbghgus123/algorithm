# 문제 : https://www.acmicpc.net/problem/1038

import sys
input = sys.stdin.readline

n = int(input())
answer = [0]

def dfs(arr, length):
    if len(arr) == length:
        answer.append(int(''.join(map(str, arr))))
    else:
        if arr:
            for i in range(arr[-1]):
                dfs(arr + [i], length)
        else:
            for i in range(10):
                dfs([i], length)

for i in range(1, 11):
    dfs([], i)
if n > 1023:
    print(-1)
else:
    print(answer[n])