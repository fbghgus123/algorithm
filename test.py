import math

n = int(input())
room = list(map(int,input().split()))
a, b = map(int, input().split())
answer = 0
for i in room:
    num = i - a
    count = 1
    if num > 0:
        count += math.ceil(num / b)
    print(count)
    answer += count
print(answer)