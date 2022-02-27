# 문제 : https://programmers.co.kr/learn/courses/30/lessons/12927#qna

import heapq
def solution(n, works):
    works = list(map(lambda x : -x, works))
    heapq.heapify(works)
    
    for _ in range(n):
        tmp = heapq.heappop(works)
        if tmp != 0:
            tmp += 1
        heapq.heappush(works, tmp)
    
    return sum(map(lambda x : x ** 2, works))