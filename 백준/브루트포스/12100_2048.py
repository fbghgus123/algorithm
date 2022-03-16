import sys
import copy

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]

def upDown(d, grid):
    for i in range(n):
        stack = []
        tmp = []
        for j in range(n):
            if grid[j][i] == 0: continue
            if stack and stack[-1] == grid[j][i]:
                tmp.append(stack.pop() * 2)
            else:
                if stack: tmp.append(stack.pop())
                stack.append(grid[j][i])
        while stack: tmp.append(stack.pop())
        for j in range(n - len(tmp)):
            if d == 0:
                tmp.append(0)
            else:
                tmp.insert(0, 0)
        for j in range(n):
            grid[j][i] = tmp[j]
    return grid

def leftRight(d, grid):
    for i in range(n):
        stack = []
        tmp = []
        for j in range(n):
            if grid[i][j] == 0: continue
            if stack and stack[-1] == grid[i][j]:
                tmp.append(stack.pop() * 2)
            elif grid[i][j] != 0:
                if stack: tmp.append(stack.pop())
                stack.append(grid[i][j])
        while stack: tmp.append(stack.pop())
        for j in range(n - len(tmp)):
            if d == 0:
                tmp.append(0)
            else:
                tmp.insert(0, 0)
        for j in range(n):
            grid[i][j] = tmp[j]
    return grid
maxx = 0
s = []
def dfs(count):
    global s
    tmp = copy.deepcopy(count)
    if len(count) == 5:
        s.append(tmp)
    else:
        for i in range(4):
            dfs(tmp + [i])
dfs([])

for i in s:
    tmp = copy.deepcopy(mapp)
    for j in i:
        if j == 0:
            tmp = upDown(0, tmp)
        elif j == 1:
            tmp = upDown(1, tmp)
        elif j == 2:
            tmp = leftRight(0, tmp)
        else:
            tmp = leftRight(1, tmp)
    for j in range(n):
        maxx = max(maxx, max(tmp[j]))
print(maxx)