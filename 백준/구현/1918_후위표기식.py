# 문제 : https://www.acmicpc.net/problem/1918

string = input()

s = []
output = []

def precedence(op):
    if op == '(' or op == ')': return 3
    elif op == '+' or op == '-': return 2
    elif op == '*' or op == '/': return 1

for term in string:
    if term in '(':
        s.append('(')
    elif term in ')':
        while s:
            tmp = s.pop()
            if tmp == '(': break
            output.append(tmp)
    elif term in '+-*/':
        while s:
            if precedence(s[-1]) <= precedence(term):
                output.append(s.pop())
            else: break
        s.append(term)
    else:
        output.append(term)

while s: output.append(s.pop())

print(''.join(output))