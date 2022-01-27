import bisect

num = [0,1,2,3,4,5,6,7,8,9]

print(bisect.bisect_left(num, 5)) # 5의 가장 왼쪽 인덱스를 반환
print(bisect.bisect_right(num, 5)) # 5의 가장 오른쪽 인덱스를 반환