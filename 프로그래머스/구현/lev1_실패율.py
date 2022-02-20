def solution(N, stages):
    fail = []
    for i in range(1, N+1):
        cl = 0
        non = 0
        for j in stages:
            if j >= i:
                cl += 1
            if j == i:
                non += 1
        if cl != 0:
            fail.append(non / cl)
        else:
            fail.append(0)
    failure = []
    for i in range(N):
        failure.append((i+1, fail[i]))
    failure = sorted(failure, key = lambda x : -x[1])
    return list(map(lambda x : x[0], failure))