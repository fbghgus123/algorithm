# 문제 : https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
numsS = sorted(list(set(nums)))
indexes = dict()
count = 0

for i in numsS:
    indexes[i] = count
    count += 1

print(' '.join(map(lambda x : str(indexes[x]), nums)))