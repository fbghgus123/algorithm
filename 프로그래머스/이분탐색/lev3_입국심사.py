# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in times:
            count += mid // i
        
        if n <= count:
            end = mid - 1
        else:
            start = mid + 1
        
        print(start, end, mid, count)
    
    return start