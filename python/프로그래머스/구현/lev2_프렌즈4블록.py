# 문제: https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    board = list(map(list, board))
    def check():
        where = []
        for i in range(m-1):
            for j in range(n-1):
                tmp = board[i][j]
                if tmp == board[i][j] and tmp == board[i][j+1] and tmp == board[i+1][j] and tmp == board[i+1][j+1] and tmp != '0':
                    where.append((i, j))
        return where
    
    def delete(v):
        y, x = v
        board[y][x] = 0
        board[y+1][x] = 0
        board[y][x+1] = 0
        board[y+1][x+1] = 0
        
    def goDown():
        new = []
        for i in range(n):
            tmp = ''
            for j in range(m):
                if board[j][i] != 0:
                    tmp += board[j][i]
            new.append(tmp.zfill(m))
        
        realNew = [[] for _ in range(m)]
        for i in range(n):
            for j in range(1,m+1):
                realNew[m-j].append(new[i][m-j])
        return realNew
    
    while check():
        for i in check():
            delete(i)
        board = goDown()
    answer = 0
    for i in board:
        answer += i.count('0')
    return answer