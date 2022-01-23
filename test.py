n, k = map(int, input().split())
bag = []
for _ in range(n):
    w, v = map(int, input().split())
    bag.append([w, v])
bag = sorted(bag, key = lambda x : -x[1]/x[0])

print(bag)

value = 0
for i in bag:
    if k-i[0] >= 0:
        k -= i[0]
        value += i[1]

print(value)