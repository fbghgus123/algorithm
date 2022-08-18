# 문제 : https://www.acmicpc.net/problem/16198

n = int(input())
w = list(map(int, input().split()))
maxx = 0

def energy(arr, e):
    global maxx
    if len(arr) < 3 and maxx < e:
        maxx = e
        return
    for i in range(1, len(arr)-1):
        energy(arr[:i] + arr[i+1:len(arr)], e + arr[i-1] * arr[i+1])

energy(w, 0)
print(maxx)