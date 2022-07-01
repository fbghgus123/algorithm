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
    
    
        

    

