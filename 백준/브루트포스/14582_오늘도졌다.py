# 문제: https://www.acmicpc.net/problem/14582

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = False

sumA = 0
sumB = 0

for i in range(9):
    sumA += a[i]
    if sumA > sumB:
        result = True
        break
    sumB += b[i]

if result:
    print('Yes')
else:
    print('No')