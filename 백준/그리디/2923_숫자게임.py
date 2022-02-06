import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
for i in range(1, n+1):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)
    a.sort()
    b.sort()

    if a[-1] > b[-1]:
        big = a[-1] + b[0]
    elif a[-1] < b[-1]:
        big = a[0] + b[-1]
    else:
        c = a + b
        c.sort()
        print(c)