# 문제 : https://programmers.co.kr/learn/courses/30/lessons/92341?language=python3

from collections import defaultdict
import math

def convertMinute(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def solution(fees, records):
    record = defaultdict(int)
    stackTime = defaultdict(int)
    
    defaultTime, defaultCost, unitTime, unitCost = fees
    records = map(lambda x:x.split(), records)
    for time, num, io in records:
        if io == "IN":
            record[num] = convertMinute(time)
        else:
            stackTime[num] += convertMinute(time) - record[num]
            del record[num]
    
    for k, v in record.items():
        stackTime[k] += 1439 - v
    
    answer = []
    for num in sorted(list(stackTime)):
        time = stackTime[num]
        time -= defaultTime
        total = defaultCost
        if time > 0: total += math.ceil(time/unitTime) * unitCost
        answer.append(total)
    return answer
    