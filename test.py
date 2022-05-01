N, K = map(int, input().split())
b = []
for i in range(N):
    b.append(int(input()))
total = 0
b.reverse()

for i in range(N):
    if K >= b[i]:
        a = K // b[i]
        K = K % b[i]
        total += a
print(total)