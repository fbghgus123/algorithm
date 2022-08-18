# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42890

import itertools
def solution(relation):
    answer = 0
    n = len(relation[0])
    attribute = [i for i in range(n)]

    combi = []
    for i in range(1, n+1):
        tmp = itertools.combinations(attribute, i)
        [combi.append(j) for j in tmp]
    
    while combi:
        indexs = combi.pop(0)
        if check(indexs, relation):
            answer += 1
            combi = del_combi(indexs, combi)
    return answer

def del_combi(index, combi):
    tmp = []
    for i in combi:
        flag = False
        for j in index:
            if j not in i:
                flag = True
        if flag: tmp.append(i)
    return tmp

def check(index, relation):
    visited = []
    for i in range(len(relation)):
        tmp = []
        for j in index:
            tmp.append(relation[i][j])
        if tmp in visited:
            return False
        visited.append(tmp)
    return True