# 정답 코드

from itertools import permutations

n = int(input())
water = list(map(int, input().split()))
discountInfo = []

for _ in range(n):
    tmp = []
    nn = int(input())
    for _ in range(nn):
        tmp.append(list(map(int, input().split())))
    discountInfo.append(tmp)

result = 10001
for order in list(permutations(range(n), n)):
    answer = 0
    tmp = water.copy()

    for current in order:
        answer += tmp[current]
        for i in discountInfo[current]:
            tmp[i[0]-1] -= i[1]
            if tmp[i[0]-1] < 1: tmp[i[0]-1] = 1
    result = min(result, answer)
print(result)