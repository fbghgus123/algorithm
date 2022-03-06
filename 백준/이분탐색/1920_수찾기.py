# 문제 : https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    start, end = 0, len(nums)-1
    flag = True
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            print(1)
            flag = False
            break
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if flag: print(0)