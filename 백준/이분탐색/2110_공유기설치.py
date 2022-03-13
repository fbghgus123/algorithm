# 문제 : https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

start = home[0]
end = home[-1] - home[0]

while start < end:
    mid = start + end // 2
    tmp = home[0]
    count = 1

    for i in range(1, len(home)):
        if home[i] >= mid + tmp:
            count += 1
            tmp = home[i]

    if count >= c:
        start = mid + 1
    else:
        end = mid - 1
print(mid)