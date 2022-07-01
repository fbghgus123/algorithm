from itertools import permutations

field = [0, 0, 0]

def hit1(field):
    global score
    score += sum(field[:1])
    field = field[1:] + [1]
    return field

def hit2(field):
    global score
    score += sum(field[:2])
    field = field[2:] + [1, 0]
    return field

def hit3(field):
    global score
    score += sum(field[:3])
    field = [1, 0, 0]
    return field

def homerun(field):
    global score
    score += sum(field) + 1
    field = [0, 0, 0]
    return field

n = int(input())
for i in permutations(list(range(8)), 8):
    print(i)