# 문제 : https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), key=lambda x : -x)

s = 0
for i in range(n):
    s += a.pop() * b.pop()
print(s)