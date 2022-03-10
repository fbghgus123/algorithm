n, k = map(int, input().split())
i = 0
while n > 2 ** i:
    i += 1

for j in range(i-1,-1,-1):
    if n > 2 ** j:
        k -= 1
        n -= 2 ** j
print(2**j, n)
print(2**j - n)