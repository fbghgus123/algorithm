# 문제 : https://programmers.co.kr/learn/courses/30/lessons/72411

import itertools

def solution(orders, course):
    menu = dict()
    for order in orders:
        for count in course:
            for i in itertools.combinations(order, count):
                tmp = ''.join(sorted(i))
                if tmp in menu:
                    menu[tmp] += 1
                else:
                    menu[tmp] = 1
    
    answer = []
    for count in course:
        a = filter(lambda x : len(x[0]) == count and x[1] > 1, menu.items())
        a = sorted(a, key=lambda x:(-x[1], x[0]))
        for i in a:
            if i[1] == a[0][1]:
                answer.append(i[0])
            else:
                break
    return sorted(answer)