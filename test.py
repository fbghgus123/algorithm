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
