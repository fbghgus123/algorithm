# 문제 : https://www.acmicpc.net/problem/10250

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    num = n // h + 1

    if floor == 0:
        floor = h
        num = n // h
    print(floor*100 + num)