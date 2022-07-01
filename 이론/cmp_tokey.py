from functools import cmp_to_key
# functools.cmp_to_key(func) 함수는 sorted와 같은 정렬 함수의 key 
# 매개변수에 함수(func)를 전달할 때 사용하는 함수이다. 
# 단, func 함수는 두 개의 인수를 받아들이고, 첫번째 인수를 기준으로 그들을 비교하여, 
# 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수이어야 한다.

def xy_compare(n1, n2):
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=cmp_to_key(xy_compare))
print(result)