# unpacking
# 리스트 앞에 *를 붙여 언패킹
a = [3, 4, 5, 6]
print(*a)

# 딕셔너리 잘 쓰기
# zip : 각 iterables의 요소들을 묶어주는 iterables를 반환
b = ['삼', '사', '오', '육']
print(*zip(a, b))
_dict = dict(zip(a, b))
print(_dict)
# setdefault: 딕셔너리에 값이 있을 땐 해당 값을 리턴, 값이 없을 땐 디폴트 값을 리턴
print(_dict.setdefault(7, '칠'))
# 딕셔너리 언패킹
print(*_dict.keys())
print(*_dict.values())
print(*_dict.items())

# 조건 여러 개 sorting -> key 값을 튜플 형태로 묶어줌
_list = [(2, 4), (2, 3), (1, 5), (3, 2), (2, 6)]
# 0번 인덱스로 오름차순 1번 인덱스로 내림차순 정렬
sorted_list = sorted(_list, key = lambda dt: (dt[0], -dt[1]))
print(sorted_list)

# 문자열 뒤집기
string = 'I am Hungry...'
print(string[::-1])
print("".join(reversed(string)))

# for 문에서 인덱스와 값 가져오기
for idx, val in enumerate(a):
    print(idx, val)

# 문자열에 들어간 문자 세기
from collections import Counter
print(Counter('Hello world').most_common()) # 전체를 리스트로 리턴
print(Counter('Hello world').most_common(2)) # 상위 2개를 리스트로 리턴

# 배열 회전 하기
def rotate(arr):
    return list(zip(*arr[::-1]))
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [(7, 4, 1), (8, 5, 2), (9, 6, 3)]