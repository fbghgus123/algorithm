n = int(input())
count = -1
def calc(arr, depth):
    global count
    if depth == len(arr):
        count += 1
        if count == n:
            print(''.join(map(str, arr)))
            return
    else:
        for i in range(10):
            if not arr or arr[-1] > i:
                calc(arr + [i], depth)
# if n > 1023:
#     print(-1)
# else:
for i in range(1, 11):
    calc([], i)