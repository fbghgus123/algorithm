# 배열 한 개 에서 값이 있는 제일 마지막 인덱스
def getLastIndex(arr, n):
    result = -1
    for index in range(n-1, -1, -1):
        if arr[index] > 0:
            result = index
            break
    return result

# 배달/수거 중 제일 멀리 이동해야할 값 구함
def getMovement(dil, gc, n):
    a = getLastIndex(dil, n)
    b = getLastIndex(gc, n)
    return max(a, b)

# 배열에서 젤 마지막 순서로 cap 만큼 제거
def removeLast(arr, num, n):
    for i in range(n-1, -1, -1):
        if arr[i] > 0:
            amount = min(arr[i], num)
            num -= amount
            arr[i] -= amount
        if num == 0: return


def solution(cap, n, deliveries, pickups):
    answer = 0
    n = getMovement(deliveries, pickups, n) + 1

    while 1 :
        removeLast(deliveries, cap, n)
        removeLast(pickups, cap, n)
        answer += n * 2
        n = getMovement(deliveries, pickups, n) + 1
        if n == 0: break

    return answer

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

answer = solution(cap, n, deliveries, pickups)
print(answer)