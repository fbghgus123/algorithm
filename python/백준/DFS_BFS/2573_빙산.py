import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
after = [[0] * m for _ in range(n)]
year = -1
dx, dy = [1,-1,0,0], [0,0,1,-1]

def dfs(v):
    i, j = v[0], v[1]
    if ice[i][j] != 0:
        count = 0
        for z in range(4):
            cx = i + dx[z]
            cy = j + dy[z]
            if 0 <= cx < n and 0 <= cy < m:
                if ice[cx][cy] == 0:
                    count += 1
                elif check[cx][cy] == 0:
                    check[cx][cy] = 1
                    dfs((cx, cy))
        after[i][j] = ice[i][j] - count if ice[i][j] - count > 0 else 0

while(1):
    num = 0
    for i in ice:
        num += sum(i)
    if num <= 0:
        print(0)
        break

    year += 1
    check = [[0] * m for _ in range(n)]
    after = [[0] * m for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(m):
            if check[i][j] == 0 and ice[i][j] > 0:
                if not flag:
                    flag = True
                    dfs((i,j))
                else:
                    print(year)
                    exit()
    ice = after.copy()