# 문제: https://www.acmicpc.net/problem/2096
# 도움된 글: https://rhdtka21.tistory.com/48?category=826388

from ipaddress import ip_address
import sys
input = sys.stdin.readline

n = int(input())

up = [[0] * 3 for _ in range(2)]
down = [[0] * 3 for _ in range(2)]

for i in range(n):
    temp = list(map(int, input().split()))

    up[1][0] = max(up[0][0], up[0][1]) + temp[0]
    up[1][1] = max(up[0][0], up[0][1], up[0][2]) + temp[1]
    up[1][2] = max(up[0][1], up[0][2]) + temp[2]

    down[1][0] = min(down[0][0], down[0][1]) + temp[0]
    down[1][1] = min(down[0][0], down[0][1], down[0][2]) + temp[1]
    down[1][2] = min(down[0][1], down[0][2]) + temp[2]

    down[0][0], down[0][1], down[0][2] = down[1][0], down[1][1], down[1][2]
    up[0][0], up[0][1], up[0][2] = up[1][0], up[1][1], up[1][2]

print(max(up[1]), min(down[1]))