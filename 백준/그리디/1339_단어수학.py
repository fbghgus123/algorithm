# 문제 : https://www.acmicpc.net/problem/1339

from calendar import LocaleTextCalendar
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
letter = defaultdict(int)
for _ in range(n):
    word = input().strip()
    for i in range(len(word)):
        letter[word[len(word)-i-1]] += 10**i

sum = 0
num = 9
for i in sorted(letter.values(), reverse=True):
    sum += i * num
    num -= 1
print(sum)