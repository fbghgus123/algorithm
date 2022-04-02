from collections import deque
import sys
sys.setrecursionlimit(100000)

maxx = 1_000_000_007
n = int(input())
string = input()
dp = [0] * n
fibb = [0] * 200_001
fibb[0] = 1
fibb[1] = 1
e = deque()
answer = 0

def fib(n):
    if fibb[n]: return fibb[n]
    fibb[n] = n * fib(n-1)
    return fibb[n]

def choose(n, c):
    return fib(n) // (fib(c) * fib(n-c))

for i in range(n):
    if string[i] == 'W':
        for j in range(i, n):
            if string[j] == 'H':
                dp[j] += 1
    
    if string[i] == 'H':
        for j in range(i, n):
            if string[j] == 'E':
                dp[j] += dp[i]

    if string[i] == 'E':
        e.append(i)

while e:
    tmp = e.popleft()
    lastE = 0
    for i in range(1, len(e)+1):
        lastE += choose(len(e), i)
    lastE %= maxx
    answer += lastE * dp[tmp] % maxx
print(answer % maxx)