# 문제: https://www.acmicpc.net/problem/5430

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    a = input().strip().strip('[').strip(']').split(',')
    if a[0] == '':
        a = []
    text = '['
    b = True
    for i in p:
        if i == 'D':
            if not a:
                a = 'error'
                break
            if b:
                a.pop(0)
            else:
                a.pop()
        else:
            b = not b
    if a == 'error':
        print(a)
        continue
    if b:
        text += ','.join(a)
    else:
        text += ','.join(a[::-1])
    print(text+']')