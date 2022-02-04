# 문제: https://www.acmicpc.net/problem/2621

import sys
input = sys.stdin.readline

colors = []
number = []
card = dict()

for _ in range(5):
    color, num = input().split()
    num = int(num)
    colors.append(color)
    number.append(num)
    if num in card: card[num] += 1
    else: card[num] = 1
number.sort()

colors = True if colors.count(color) == 5 else False
for i,v in enumerate(number):
    straight = True
    if i < 4 and v+1 != number[i+1]:
        straight = False
        break
same = []
for i in range(5):
    same.append(number.count(number[i]))
same = list(set(same))

fourCard = True if max(same) == 4 else False
fullHouse = True if 3 in same and 2 in same else False

onePair = True if len(set(number)) == 4 else False

if colors and straight:
    score = number[4] + 900
elif fourCard:
    score = number[2] + 800
elif fullHouse:
    score = number[0] * 10 + number[4] + 700
elif colors:
    score = number[4] + 600
elif straight:
    score = number[4] + 500
elif 3 in same:
    score = number[2] + 400
else:
    two = []
    for i, v in card.items():
        if v == 2: two.append(i)
    two.sort()
    if len(two) == 2:
        score = two[1]*10 + two[0] + 300
    elif len(two) == 1:
        score = two[0] + 200
    else:
        score = number[4] + 100
print(score)