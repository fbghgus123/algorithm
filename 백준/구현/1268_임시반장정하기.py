# 문제: https://www.acmicpc.net/problem/1268

import sys
input = sys.stdin.readline

n = int(input())
student = [list(map(int, input().split())) for _ in range(n)]
friend = [[] for _ in range(n)]


for i in range(5):
    for j in range(n):
        for e in range(n):
            if j != e and student[j][i] == student[e][i]:
                friend[j].append(e)

friend = list(map(lambda x : len(list(set(x))), friend))
print(friend.index(max(friend))+1)