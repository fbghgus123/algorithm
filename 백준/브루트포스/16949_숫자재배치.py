# 문제 : https://www.acmicpc.net/problem/16943

a, b = map(int, input().split())

a = list(map(int, list(str(a))))
maxx = 0

def dfs(select, current):
    global maxx
    if len(select) == len(a):
        num = int(''.join(map(str, select)))
        if maxx < num < b:
            maxx = num

    for i in range(len(current)):
        if not select and current[i] == 0:
            continue
        dfs(select + [current[i]], current[:i] + current[i+1:])

dfs([], a)
if maxx == 0:
    print(-1)
else:
    print(maxx)