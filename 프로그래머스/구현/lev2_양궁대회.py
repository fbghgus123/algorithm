# 문제 : https://programmers.co.kr/learn/courses/30/lessons/92342
# 도움된 글 : https://velog.io/@jadenkim5179/프로그래머스-양궁대회

from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):
        cnt = Counter(comb)
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10-i] < cnt[i]:
                score1 += i
            elif info[10-i] > 0:
                score2 += i
                
        diff = score1 - score2
        if diff > max_diff:
            max_comb_cnt = cnt
            max_diff = diff
            
    if max_diff > 0:
        answer = [0]*11
        for n in max_comb_cnt:
            answer[10-n] = max_comb_cnt[n] 
        return answer 
    else:
        return [-1]