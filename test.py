from collections import deque
grid = [list(input()) for _ in range(8)]

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

print(bfs())