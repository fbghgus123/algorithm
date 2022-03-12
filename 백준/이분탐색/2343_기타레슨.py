# 문제 : https://www.acmicpc.net/problem/2343
# 도움된 글 : https://deok2kim.tistory.com/109

n, m = map(int, input().split())
bluelay = list(map(int, input().split()))

start = max(bluelay)
end = sum(bluelay)

while start <= end:
    mid = (start + end) // 2
    
    tmp = 0
    count = 1
    for i in bluelay:
        if tmp + i <= mid:
            tmp += i
        else:
            count += 1
            tmp = i
    if count > m:
        start = mid + 1
    elif count <= m:
        end = mid - 1
print(start)