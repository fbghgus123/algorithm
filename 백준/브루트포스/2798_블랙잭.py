import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

a = list(itertools.combinations(card, 3))
max = 0
for i in a:
    if sum(i) > max and sum(i) <= m:
        max = sum(i)
print(max)