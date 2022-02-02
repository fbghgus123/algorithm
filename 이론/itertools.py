import itertools

a = [1,2,3,4,5]

print(list(itertools.combinations(a, 2))) # 조합
print(list(itertools.permutations(a, 2))) # 순열
print(list(itertools.combinations_with_replacement(a, 2))) # 중복을 포함한 조합
print(list(itertools.product(a, repeat=2))) # 중복을 포함한 순열