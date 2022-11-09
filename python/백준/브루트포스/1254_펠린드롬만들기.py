# 문제 : https://www.acmicpc.net/problem/1254

s = input()
if s == s[::-1]:
    print(len(s))
else:
    for i in range(1, len(s)+1):
        tmp = s + s[:i][::-1]
        if tmp == tmp[::-1]:
            print(len(tmp))
            break