#  문제: https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3

def solution(routes):
    routes = map(lambda x : [int(-x[0]), int(-x[1])], routes)
    routes = sorted(routes, key=lambda x : -x[0], reverse=True)
    count = 0
    while routes:
        count += 1
        tmp = routes[0][0]
        routes = list(filter(lambda x : x[1] > tmp, routes))
    return count