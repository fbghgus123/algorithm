import sys
input = sys.stdin.readline

n = int(input())
rank = [int(input()) for _ in range(n)]
rank.sort()
count = 0
for i in range(n):
    count += abs(rank[i] - (i+1))
print(count)