# 문제 : https://www.acmicpc.net/problem/14888

import sys
import math

n = int(input())
maxx = -sys.maxsize
minn = sys.maxsize
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

def dfs(index, op, num):
    global maxx, minn
    if index == n:
        maxx = max(maxx, num)
        minn = min(minn, num)
    for i in range(4):
        tmp = op.copy()
        if op[i] >= 1:
            if i == 0:
                tmp[0] -= 1
                dfs(index+1, tmp, num + nums[index])
            elif i == 1:
                tmp[1] -= 1
                dfs(index+1, tmp, num - nums[index])
            elif i == 2:
                tmp[2] -= 1
                dfs(index+1, tmp, num * nums[index])
            else:
                tmp[3] -= 1
                if num < 0:
                    dfs(index+1, tmp, math.ceil(num / nums[index]))
                else:
                    dfs(index+1, tmp, num // nums[index])
dfs(1, operators, nums[0])
print(maxx)
print(minn)