# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict
def solution(record):
    answer = []
    nickname = defaultdict(str)
    for i in record:
        i = i.split()
        if i[0] != "Leave" and i[2] != nickname[i[1]]:
            nickname[i[1]] = i[2]

    for i in record:
        i = i.split()
        if i[0] == 'Enter':
            answer.append("{0}님이 들어왔습니다.".format(nickname[i[1]]))
        elif i[0] == 'Leave':
            answer.append("{0}님이 나갔습니다.".format(nickname[i[1]]))
    return answer