# 문제: https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    timetable = sorted(list(map(lambda x : int(x[:2]) * 60 + int(x[3:5]), timetable)))
    bus = 540
    busTime = []
    passenger = []
    for _ in range(n):
        busTime.append(bus)
        bus += t
    for i in busTime:
        tmp = []
        for _ in range(m):
            if timetable and timetable[0] <= i:
                tmp.append(timetable.pop(0))
            else:
                break
        passenger.append(tmp)
    
    bus = passenger.pop()
    if len(bus) < m:
        answer = busTime.pop()
    else:
        answer = list(set(bus)).pop() - 1
    return "{0}:{1}".format(str(answer//60).zfill(2), str(answer%60).zfill(2))