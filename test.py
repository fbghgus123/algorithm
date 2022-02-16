import math
n, kim, lim = map(int, input().split())
for i in range(math.ceil(n ** 0.5)):
    if min(kim, lim) % 2 == 1 and abs(kim - lim) == 1:
        a = False
        print(i + 1)
        break
    else:
        kim = math.ceil(kim/2)
        lim = math.ceil(lim/2)
