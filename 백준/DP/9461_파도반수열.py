# 문제: https://www.acmicpc.net/problem/9461
# P(N) = P(N-1) + P(N-5)
import sys
input = sys.stdin.readline
m = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
max = 10
t = int(input())
for _ in range(t):
    n = int(input())
    if n > max:
        for k in range(max + 1, n+1):
            max += 1
            m.append(m[k-1] + m[k-5])
    print(m[n])
        
