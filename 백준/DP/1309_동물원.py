# 문제: https://www.acmicpc.net/problem/1309

import sys
input = sys.stdin.readline

n = int(input())
a = [[0]*3 for _ in range(n)]
a[0] = [1]*3

for i in range(1, n):
    a[i][0] = (a[i-1][1] + a[i-1][2] + a[i-1][0]) % 9901
    a[i][1] = (a[i-1][0] + a[i-1][2]) % 9901
    a[i][2] = (a[i-1][0] + a[i-1][1]) % 9901

print(sum(a[n-1]) % 9901)