# 문제: https://www.acmicpc.net/problem/1890
# 도움된 글: https://deok2kim.tistory.com/189

# DP 풀이
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dp = [[0] * N for _ in range(N)]  # i,j까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:  # 끝에 도달했을 때
            print(dp[i][j])
            break
        cur_cnt = field[i][j]
        # 오른쪽으로 가기
        if j + cur_cnt < N:
            dp[i][j + cur_cnt] += dp[i][j]
        # 아래로 가기
        if i + cur_cnt < N:
            dp[i + cur_cnt][j] += dp[i][j]
# BFS 풀이: 메모리 초과 발생
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# pan = [list(map(int, input().split())) for _ in range(n)]

# count = 0
# queue = deque()
# queue.append((0,0))

# while queue:
#     x, y = queue.popleft()
#     long = pan[y][x]

#     if x == n-1 and y == n-1:
#         count += 1

#     if x + long < n and long != 0:
#         isPass = True
#         for i in range(1, long):
#             if pan[y][x+i] == 0:
#                 isPass = False
#                 break
#         if isPass: queue.append((x+long, y))
    
#     if y + long < n and long != 0:
#         isPass = True
#         for i in range(1, long):
#             if pan[y+i][x] == 0:
#                 isPass = False
#                 break
#         if isPass: queue.append((x, y+long))

# print(count)
