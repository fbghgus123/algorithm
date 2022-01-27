# input() 보다 sys.stdin.readline 이 더 빠르다 !
# 테스트 1부터 100까지의 수

import sys
input = sys.stdin.readline

print(map(int, input().split ()))