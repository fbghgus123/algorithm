n = int(input())

chess = [0] * (n+1)
def dfs(chess, a):
    print(chess)
    if a == n+1:
        print(chess)
        return
    for i in range(1, n+1):
        tmp = chess.copy
        if i not in chess:
            flag = False
            for j in range(1, len(chess)):
                if chess[j] != 0 and abs(chess[j]-i) == abs(a-j):
                    flag = True
                    break
            if flag: continue
            tmp[a] = i
            dfs(tmp, a+1)

dfs(chess, 1)