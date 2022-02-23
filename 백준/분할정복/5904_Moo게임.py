# 문제 : https://www.acmicpc.net/problem/5904
# 도움된 글 : https://tesseractjh.tistory.com/101

N = int(input())

def moo(acc, cur, N):
    prev = (acc-cur)//2
    if N <= prev: return moo(prev, cur-1, N)
    elif N > prev+cur: return moo(prev, cur-1, N-prev-cur)
    else: return "o" if N-prev-1 else "m"

acc, n = 3, 0
while N > acc:
    n += 1
    acc = acc*2+n+3

print(moo(acc, n+3, N))