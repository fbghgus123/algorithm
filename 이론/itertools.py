import itertools

a = [1,2,3,4,5]

print(list(itertools.combinations(a, 2))) # 조합
print(list(itertools.permutations(a, 2))) # 순열