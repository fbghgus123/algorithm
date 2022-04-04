# 문제 : https://www.acmicpc.net/problem/9663

n = int(input())
answer = 0
chess = [-1] * n

def dfs(chess, row):
    global answer
    cant = set()
    if row == n+1:
        answer += 1
        return
    for i in range(n):
        if chess[i] != -1:
            distance = row - chess[i]
            if i - distance >= 0: cant |= {i - distance}
            if i + distance < n: cant |= {i + distance}
    for i in range(n):
        if chess[i] == -1 and i not in cant:
            tmp = chess.copy()
            tmp[i] = row
            dfs(tmp, row+1)

dfs(chess, 1)
print(answer)