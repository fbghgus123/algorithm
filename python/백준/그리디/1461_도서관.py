# 문제: https://www.acmicpc.net/problem/1461

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

answer = 0

minusBook = [book for book in books if book < 0]
plusBook = [book for book in books if book > 0]
plusBook.reverse()

if minusBook and plusBook and abs(minusBook[0]) > plusBook[0]:
    answer += abs(minusBook[0])
    for _ in range(m):
        if minusBook:
            minusBook.pop(0)
else:
    if plusBook:
        answer += plusBook[0]
        for _ in range(m):
            if plusBook:
                plusBook.pop(0)
    elif minusBook:
        answer += abs(minusBook[0])
        for _ in range(m):
            if minusBook:
                minusBook.pop(0)

def calc(books):
    global answer
    while(books):
        if len(books) > m:
            answer += abs(books[0]) * 2
            books = books[m:]
        else:
            answer += abs(books[0]) * 2
            break
    return books
minusBook = calc(minusBook)
plusBook = calc(plusBook)
print(answer)