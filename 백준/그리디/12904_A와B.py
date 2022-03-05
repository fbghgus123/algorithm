# 문제 : https://www.acmicpc.net/problem/12904
# 도움된 글 : https://chocochip101.tistory.com/entry/백준-12904번-파이썬-A와-B

s = list(input())
t = list(input())
flag = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        flag = True
        break
print(1 if flag else 0)