# 문제 : https://programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    stack = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            stack[r1][c1] -= degree
            stack[r1][c2+1] += degree
            stack[r2+1][c1] += degree
            stack[r2+1][c2+1] -= degree
        elif t == 2:
            stack[r1][c1] += degree
            stack[r1][c2+1] -= degree
            stack[r2+1][c1] -= degree
            stack[r2+1][c2+1] += degree
    for i in range(len(stack)):
        for j in range(1, len(stack[0])):
            stack[i][j] += stack[i][j-1]

    for j in range(len(stack[0])):
        for i in range(1, len(stack)):
            stack[i][j] += stack[i-1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if stack[i][j] + board[i][j] > 0:
                answer += 1
    return answer