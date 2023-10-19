# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/136797

MAX_VALUE = 700_000

def solution(numbers):
    scores = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3], # 0
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], # 1
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], # 2
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], # 3
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], # 4
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], # 5
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], # 6
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], # 7
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], # 8
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1], # 9
    ]
    
    length = len(numbers)
    first_number = int(numbers[0])
    dp = [[MAX_VALUE for _ in range(100)] for _ in range(length)]
    
    dp[0][first_number * 10 + 6] = scores[4][first_number]
    dp[0][4 * 10 + first_number] = scores[6][first_number]
    
    for idx, num in enumerate(numbers):
        if idx == 0: continue
        current_num = int(num)
        
        for i in range(0, 10):
            for j in range(0, 10):
                if i == j: continue
                dp[idx][i * 10 + current_num] = min(dp[idx][i * 10 + current_num], dp[idx-1][i * 10 + j] + scores[j][current_num])
                dp[idx][current_num * 10 + j] = min(dp[idx][current_num * 10 + j], dp[idx-1][i * 10 + j] + scores[i][current_num])
    
    answer = MAX_VALUE
    for i in range(0, 10):
        for j in range(0, 10):
            answer = min(answer, dp[length - 1][i * 10 + j])
                
    
    return answer