n, l = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def check(arr):
    stair = [0] * len(arr)
    for _ in range(2):
        for i, v in enumerate(arr):
            if i < n-1 and arr[i] - arr[i+1] > 1: return False
            if i < n-1 and arr[i] - arr[i+1] == 1:
                if n - i <= l: return False # 남은 개수 확인
                for k in range(i+1, i+l+1):
                    if arr[k] != arr[i] - 1 or stair[k] != 0:
                        return False
                stair[i+1:i+l+1] = [1] * l
        arr.reverse()
        stair.reverse()
    return True

answer = 0
for i in range(n):
    if check(grid[i].copy()): 
        # print("가로",i,"열",grid[i])
        answer += 1
    tmp = []
    for j in range(n):
        tmp.append(grid[j][i])
    if check(tmp): 
        # print("세로", i, "열", tmp)
        answer += 1

print(answer)