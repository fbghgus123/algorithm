# 문제: https://www.acmicpc.net/problem/12865
# 도움된 글: https://claude-u.tistory.com/208

n, k = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)] # 엑셀 만들어줌

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[n][k])