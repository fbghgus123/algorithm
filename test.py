def solution(dartResult):
    dartResult = list(dartResult)
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'#': -1, '*': 2}
    while dartResult:
        print(dartResult)
        tmp = dartResult.pop(0)
        
        if tmp == '1' and dartResult[0] == '0':
            tmp += dartResult.pop(0)
        
        score = int(tmp)
        
        tmp = dartResult.pop(0)
        score **= bonus[tmp]
        
        if dartResult[0] == '#' or dartResult[0] == '*':
            tmp = dartResult.pop(0)
            score *= option[tmp]
        print(score)

solution('1S2D*3T')