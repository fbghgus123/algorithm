# 문제 : https://www.acmicpc.net/problem/1052

n, k = map(int, input().split())
i = 0
while n > 2 ** i:
    i += 1

for j in range(i-1,-1,-1):
    if k == 1:
        break
    if n > 2 ** j and k > 1:
        k -= 1
        n -= 2 ** j
i = 0
while n > 2 ** i:
    i += 1
print(2**i - n)