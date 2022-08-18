# 문제 : https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3

import heapq

def solution(n, s, a, b, fares):
    fee = [[100_000*n] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        fee[i][i] = 0
    for S, E, c in fares:
        fee[S][E] = c
        fee[E][S] = c
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                fee[i][j] = min(fee[i][j], fee[i][k] + fee[k][j])
                
    cost = [1000_000*n] * (n+1)
    for k in range(1, n+1):
        cost[k] = fee[s][k] + fee[k][a] + fee[k][b]
    return min(cost)