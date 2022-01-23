from collections import deque
# 스택
stack = deque()
[stack.append(i) for i in range(10)] # 추가
print(stack)

a = stack.pop()
print(stack) # 맨 위에 꺼내기

#################################################
# 큐
queue = deque()
[queue.append(i) for i in range(10)] # 추가
print(queue)

a = queue.popleft() # 꺼내기
print(queue)
