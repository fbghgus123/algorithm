# 문제: https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
N = 2**(n)

dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]
count = 0

def search(n, x, y):
    global count
    tmp = n//2
    if n == 2:
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            
            if cx == c and cy == r:
                print(count)
                return    
            count += 1
        return
    
    if x <= c < x+tmp and y <= r < y+tmp: 
        search(tmp, x, y)
    elif x+tmp <= c and y <= r < y+tmp:
        count += tmp**2
        search(tmp, x + tmp, y)
    elif x <= c < x+tmp and y+tmp <= r:
        count += tmp**2 * 2
        search(tmp, x, y + tmp)
    else:
        count += tmp**2 * 3
        search(tmp, x + tmp, y + tmp)

search(N, 0, 0)
