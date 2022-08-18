# 문제 : https://www.acmicpc.net/problem/17144

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

airFilter = []

for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            airFilter.append((i, j))

def spread():
    global room
    tmp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                tmp[i][j] += room[i][j]
                dust = room[i][j] // 5
                for e in range(4):
                    x = i + dx[e]
                    y = j + dy[e]
                    if 0 <= x < r and 0 <= y < c and room[x][y] != -1:
                        tmp[x][y] += dust
                        tmp[i][j] -= dust
    room = tmp

def move():
    x, y = airFilter[0]
    for i in range(0, x):
        room[i].append(room[i+1].pop())
        room[x-i].insert(0, room[x-i-1].pop(0))
    room[x][y] = -1

    x, y = airFilter[1]
    for i in range(x, r-1):
        room[i].insert(0, room[i+1].pop(0))
        room[r+x-i-1].append(room[r+x-i-2].pop())
    room[x][y] = -1

def sumDust():
    summ = 0
    for i in range(r):
        summ += sum(room[i])
    return summ + 2

for _ in range(t):
    spread()
    move()
print(sumDust())