n, m = map(int, input().split())

def dfs(current = []):
    if len(current) == m:
        print(' '.join(map(str,current)))
    else:
        for i in range(1, n+1):
            if not current or current[-1] <= i:
                dfs(current + [i])

dfs()
