# 문제 : https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())

line = [int(input()) for _ in range(k)]
start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in line:
        count += i // mid
    
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)