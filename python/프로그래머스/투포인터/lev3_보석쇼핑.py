# 문제 : https://programmers.co.kr/learn/courses/30/lessons/67258#qna

from collections import defaultdict

def solution(gems):
    kind = defaultdict(int)
    nums = len(set(gems))
    kinds = 0
    answer = [0, len(gems)]
    
    left = 0
    for right in range(len(gems)):
        gem = gems[right]
        if kind[gem] == 0: kinds += 1
        kind[gem] += 1
        
        while(1):
            gem = gems[left]
            if kind[gem] > 1:
                kind[gem] -= 1
                left += 1
            else:
                break
        if nums == kinds and  right - left < answer[1] - answer[0]:
            answer = [left+1, right+1]
            
    return answer