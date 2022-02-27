# 문제 : https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

v = [0] * 4
h = [0] * 3

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

order = list(map(int, input().split()))
for i in order:
    tx = x + dx[i-1]
    ty = y + dy[i-1]
    if 0 <= tx < n and 0 <= ty < m:
        x = tx
        y = ty

        if i == 1:
            tmp = h.pop(0)
            h.append(v.pop())
            v.append(tmp)
            v[1] = h[1]

        elif i == 2:
            tmp = h.pop()
            h.insert(0, v.pop())
            v.append(tmp)
            v[1] = h[1]

        elif i == 3:
            v.append(v.pop(0))
            h[1] = v[1]

        elif i == 4:
            v.insert(0, v.pop())
            h[1] = v[1]

        if grid[x][y] == 0:
            grid[x][y] = v[3]
        else:
            v[3] = grid[x][y]
            grid[x][y] = 0
        
        print(v[1])
            