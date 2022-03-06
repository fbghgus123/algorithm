string = list(map(int, list(input())))
test = []
count = 0
for i in range(len(string)):
    if i == len(string)-1:
        test.append(count)
        break
    if string[i] < 3 and string[i+1] < 7:
        count += 1
    else:
        test.append(count)
        count = 0
print(test)