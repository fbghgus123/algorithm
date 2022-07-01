<<<<<<< HEAD
from collections import deque, defaultdict

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start, w, h, grid):
    dirty = []
    visited = [[0] * w for _ in range(h)]
    queue = deque()
    queue.append(start + [0])

    while queue:
        y, x, count = queue.popleft()
        for i in range(4):
            cy = y + dy[i]
            cx = x + dx[i]
            if 0 <= cy < h and 0 <= cx < w:
                if visited[cy][cx] == 0 and grid[cy][cx] != 'x':
                    visited[cy][cx] = 1
                    queue.append([cy, cx, count+1])
                    if grid[cy][cx] == '*': dirty.append((cy, cx, count+1))
    return dirty

visited = []
answer = []
def btk(current, summ):
    global distance, visited, count
    if len(visited) == count:
        answer.append(summ)
        return
    for k, v in distance[current].items():
        if k not in visited:
            visited.append(k)
            btk(k, summ + v)
            visited.pop()


while 1:
    w, h = map(int, input().split())
    if (w == 0 and h == 0): break
    count = 0

    grid = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'o': vacuum = [i, j]
            if grid[i][j] == '*': count += 1

    distance = defaultdict(dict)
    dirty = bfs(vacuum, w, h, grid)
    
    if len(dirty) != count:
        print(-1)
        continue

    for y, x, d in dirty:
        distance['vacuum'][str(y)+" "+str(x)] = d
        tmp = bfs([y, x], w, h, grid)
        for yy, xx, dd in tmp:
            distance[str(y)+" "+str(x)][str(yy)+" "+str(xx)] = dd

    answer = []
    for y, x, d in dirty:
        key = str(y)+" "+str(x)
        visited = [key]
        btk(key, distance['vacuum'][key])

    print(min(answer))
    
    
        

    

=======
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(m)]
visited = [[[-1] * n for _ in range(m)] for _ in range(4)]

c = []

for ri, row in enumerate(grid):
    for ci, v in enumerate(row):
        if v == 'C':
            c.append((ri, ci))
# 하 우 상 좌
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def bfs():
    queue = deque()
    for i in range(4):
        visited[i][c[0][0]][c[0][1]] = 0
        queue.append((*c[0], i))
    while queue:
        y, x, prev = queue.popleft()
        for i in range(4):
            cy = y + dy[i]
            cx = x + dx[i]
            if 0 <= cy < m and 0 <= cx < n:
                if grid[cy][cx] != '*':
                    if i == prev and (visited[i][cy][cx] == -1 or visited[i][cy][cx] > visited[i][y][x]):
                        visited[i][cy][cx] = visited[i][y][x]
                        queue.append((cy, cx, i))
                    if i != prev and (visited[i][cy][cx] == -1 or visited[i][cy][cx] > visited[prev][y][x] + 1):
                        visited[i][cy][cx] = visited[prev][y][x] + 1
                        queue.append((cy, cx, i))

bfs()
minn = 100000
for i in range(4):
    if visited[i][c[1][0]][c[1][1]] == -1: continue
    minn = min(minn, visited[i][c[1][0]][c[1][1]])
print(minn)
>>>>>>> b684d26c50d627f5eb595c79c4f8dcc2d851bed9
