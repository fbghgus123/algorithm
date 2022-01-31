import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input().strip() for _ in range(n)]
minn = 999

for a in range(0, n-7):
    for b in range(0, m-7):
        colect = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j)%2 == 0 and chess[i][j] == 'W':
                    colect += 1
                elif (i + j)%2 == 1 and chess[i][j] == 'B':
                    colect += 1
        colect = colect if colect < 32 else 64 - colect
        if colect < minn:
            minn = colect

print(minn)
