import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = set(list(map(int, input().split()))[1:])
party = []

def check():
    global know
    result = []
    tmp = len(know)
    for i in party:
        if i & know:
            know |= people
            if tmp != len(know):
                result = check()
        else:
            result.append(i)
    return result

for i in range(m):
    people = set(list(map(int, input().split()))[1:])
    tmp = len(know)
    party.append(people)

    if people & know:
        know |= people
        if tmp != len(know):
            party = check()
    print(party)

