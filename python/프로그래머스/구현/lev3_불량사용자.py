# 문제 : https://programmers.co.kr/learn/courses/30/lessons/64064

def check(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(len(user)):
        if user[i] == ban[i] or ban[i] == '*':
            pass
        else:
            return False
    return True

def solution(user_id, banned_id):
    ban = [[] for _ in range(len(banned_id))]
    for id in user_id:
        for i in range(len(banned_id)):
            if check(id, banned_id[i]):
                ban[i].append(id)
    
    answer = []
    
    def select(selected):
        n = len(selected)
        if n == len(banned_id):
            answer.append(selected)
            return 1
        for i in ban[n]:
            tmp = selected.copy()
            if i not in selected:
                tmp.append(i)
                select(tmp)
    select([])
    return len(set(map(lambda x : ' '.join(sorted(x)), answer)))