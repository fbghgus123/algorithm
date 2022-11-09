# 문제 : https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

from collections import deque

def solution(n, vertex):
    node = [n+1] * (n+1)
    path = [[] for _ in range(n+1)]
    
    for s, e in vertex:
        path[s].append(e)
        path[e].append(s)
        
    queue = deque()    
    queue.append(1)
    node[1] = 1
    while queue:
        v = queue.popleft()
        for i in path[v]:
            if node[i] > node[v] + 1:
                node[i] = node[v] + 1
                queue.append(i)
    node[0] = 0
    return node.count(max(node))