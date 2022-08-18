# 문제 : https://www.acmicpc.net/problem/18428

import copy
n = int(input())
grid = [input().split() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

flag = False
def look(x, y, d):
    global flag, tmp
    if grid[x][y] == 'S':
        flag = True
        return
    x += dx[d]
    y += dy[d]
    if 0 <= x < n and 0 <= y < n and tmp[x][y] != 'O':
        look(x, y, d)


def check():
    global tmp, flag
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 'T':
                flag = False
                [look(i, j, k) for k in range(4)]
                if flag: return False
    return True

def dfs(x, y, current):
    global combi
    tmp = copy.deepcopy(current)
    tmp.append((x, y))
    if len(tmp) == 3:
        combi.append(tmp)
    else:
        for i in range(y+1, n):
            if grid[x][i] == 'X': dfs(x, i, tmp)
        for i in range(x+1, n):
            for j in range(n):
                if grid[i][j] == 'X': dfs(i, j, tmp)

combi = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'X':
            dfs(i, j, [])

finded = False 
for i in combi:
    tmp = copy.deepcopy(grid)
    for x, y in i:
        tmp[x][y] = 'O'
    if check():
        finded = True
        break
if finded: print('YES')
else: print('NO')