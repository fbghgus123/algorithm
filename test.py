n, m = map(int, input().split())
memory = list(map(int, input().split()))
a = list(zip(memory.copy(), map(int, input().split())))
total = sum(memory)

dp = [[total] * (n+1) for _ in range(n+1)]


print(dp)