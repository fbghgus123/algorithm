# 문제 : https://www.acmicpc.net/problem/1092

import sys
input = sys.stdin.readline

n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
boxes = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
visited = [0 for _ in range(boxes)]
m = 0
if box[0] > crane[0]:
    m = -1
else:
    while(sum(visited) != boxes):
        tmp = 0
        m += 1
        for i in range(n):
            for j in range(tmp, boxes):
                if crane[i] >= box[j] and visited[j] == 0:
                    visited[j] = 1
                    tmp = j
                    break  
print(m)