# 문제: https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin.readline

paper = {}
count = 0
while(1):
    word = input().strip()
    if word == '': break
    if word in paper:
        paper[word] += 1
    else:
        paper[word] = 1
    count += 1

paper = list(map(lambda x : (x[0], x[1] / count * 100, 4), list(paper.items())))
paper = sorted(paper, key=lambda x : x[0])
[print('%s %.4f' % (i[0], i[1])) for i in paper]