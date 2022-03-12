# 문제 : https://www.acmicpc.net/problem/1912
# 도움된 글 : https://wook-2124.tistory.com/406

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] = max(a[i], a[i-1] + a[i])
print(max(a))