# 문제 : https://www.acmicpc.net/problem/1924

x, y = map(int, input().split())
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
for i in range(x-1):
    day += date[i]
day += y
print(week[day%7-1])