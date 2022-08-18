# 문제 : https://www.acmicpc.net/problem/13398

import copy
n = int(input())
a = list(map(int, input().split()))
b = copy.deepcopy(a)

for i in range(1, n):
    b[i] = max(a[i-1], b[i-1] + a[i])
    a[i] = max(a[i], a[i-1] + a[i])
print(max(a + b))
