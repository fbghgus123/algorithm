# 문제 : https://www.acmicpc.net/problem/1422

import sys
from functools import cmp_to_key
input = sys.stdin.readline

k, n = map(int, input().split())
n -= k
nums = [int(input()) for _ in range(k)]

def cmpSort(n1, n2):
    if int(n1+n2) > int(n2+n1):
        return -1
    elif int(n1+n2) == int(n2+n1):
        return 0
    else:
        return 1

new = nums + [max(nums)] * n
new = list(map(str, new))
new.sort(key=cmp_to_key(cmpSort))
print(''.join(new))
