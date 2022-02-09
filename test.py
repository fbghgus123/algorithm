import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
answer = []
for i in range(n):
    tmp = [a[i]]
    maxx = a[i]
    for j in range(i+1, n):
        if maxx < a[j]:
            tmp.append(a[j])
            maxx = a[j]
    answer.append(len(tmp))
print(max(answer))