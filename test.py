<<<<<<< HEAD
from collections import deque
grid = [list(input()) for _ in range(8)]
=======
<<<<<<< HEAD
import copy

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

def vertical(grid):
    result = []
    for i in range(m):
        ball = []
        for j in range(n):
            ball.append(grid[j][i])
        result.append(ball)
    return result

def reverseBox(grid):
    lines = copy.deepcopy(grid)
    for line in lines:
        line.reverse()
    return lines

def lean(lines):
    box = []
    for line in lines:
        tmpStack = []
        stack = []
        whole = False
        for v in line:
            if whole:
                stack.append(v)
                if v == 'R' or v == 'B': return v
                if v == '#':
                    whole = False
                continue
            if v == '#':
                stack += tmpStack
                tmpStack = []
                stack.append(v)
            elif v == 'R' or v == 'B':
                stack.append(v)
            elif v == 'O':
                stack += tmpStack
                tmpStack = []
                stack.append(v)
                whole = True
            else:
                tmpStack.append(v)
        stack += tmpStack
        box.append(stack)
    return box

def up(grid):
    grid = vertical(grid)
    tmp = lean(grid)
    if tmp == 'R': return True
    if tmp == 'B': return False
    grid = vertical(tmp)
    return grid

def down(grid):
    grid = vertical(grid)
    grid = reverseBox(grid)
    tmp = lean(grid)
    if tmp == 'R': return True
    if tmp == 'B': return False
    tmp = reverseBox(tmp)
    grid = vertical(tmp)
    return grid

def left(grid):
    tmp = lean(grid)
    if tmp == 'R': return True
    if tmp == 'B': return False
    grid = tmp
    return grid

def right(grid):
    grid = reverseBox(grid)
    tmp = lean(grid)
    if tmp == 'R': return True
    if tmp == 'B': return False
    tmp = reverseBox(tmp)
    grid = tmp
    return grid

answer = []
# 1: 상 2: 하 3: 좌 4: 우
def btk(count, prev):
    global grid, answer
    if count > 10: return

    box = copy.deepcopy(grid)
    if prev != 1:
        tmp = up(box)
        if tmp == True: 
            answer.append(count)
            return
        if tmp != False:
            grid = tmp
            btk(count+1, 1)
    
    if prev != 2:
        tmp = down(box)
        if tmp == True: 
            answer.append(count)
            return
        if tmp != False:
            grid = tmp
            btk(count+1, 2)

    if prev != 3:
        tmp = left(box)
        if tmp == True: 
            answer.append(count)
            return
        if tmp != False:
            grid = tmp
            btk(count+1, 3)
    
    if prev != 4:
        tmp = right(box)
        if tmp == True: 
            answer.append(count)
            return
        if tmp != False:
            grid = tmp
            btk(count+1, 4)

btk(1, 0)
print(min(answer))
=======
from itertools import permutations
>>>>>>> 096890ae06b038bc437cba13e3ab3c561fd9cda0

dx = (1, 0, -1)

def bfs():
    queue = deque()
    queue.append((7, 0))

    while queue:
        y, x = queue.popleft()
        print(y, x)
        for i in range(3):
            cy = y - 1
            cx = x + dx[i]
            if 0 <= cy < 8 and 0 <= cx < 8:
                if grid[cy][cx] != '#':
                    queue.append((cy, cx))
                if cy == 0 and cx == 7:
                    return 1
    return 0

<<<<<<< HEAD
print(bfs())
=======
def hit3(field):
    global score
    score += sum(field[:3])
    field = [1, 0, 0]
    return field

def homerun(field):
    global score
    score += sum(field) + 1
    field = [0, 0, 0]
    return field

n = int(input())
for i in permutations(list(range(8)), 8):
    print(i)
>>>>>>> 8f713bcdc344807842ffa5703a94aeba8d694e2a
>>>>>>> 096890ae06b038bc437cba13e3ab3c561fd9cda0
