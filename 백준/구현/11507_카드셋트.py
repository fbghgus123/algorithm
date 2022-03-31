# 문제 : https://www.acmicpc.net/problem/11507

from collections import defaultdict
card = defaultdict(list)

lost = input()
flag = True
for i in range(len(lost)//3):
    tmp = lost[i*3:i*3+3]
    if tmp[1:3] in card[tmp[0]]:
        flag = False
        break
    else: card[tmp[0]].append(tmp[1:3])
if flag: 
    answer = []
    for i in ['P', 'K', 'H', 'T']:
        answer.append(13 - len(card[i]))
    print(*answer)
else: print('GRESKA')
    
