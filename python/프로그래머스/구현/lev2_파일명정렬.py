# 문제 : https://programmers.co.kr/learn/courses/30/lessons/17686

import re
def solution(files):
    data = []
    for k in files:
        s = k.lower()
        head= re.match('[\D]+',s)
        number = re.search('[0-9]+',s)
        data.append((head[0], int(number[0]), k))
    result = sorted(data, key= lambda x : (x[0], x[1]))
    result = map(lambda x : x[2], result)
    return list(result)