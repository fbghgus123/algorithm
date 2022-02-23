import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hash = dict()
for _ in range(n):
    url, password = input().strip().split()
    hash[url] = password
for _ in range(m):
    url = input().strip()
    print(hash[url])