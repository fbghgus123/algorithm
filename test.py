_list = [(2, 4), (2, 3), (1, 5), (3, 2), (2, 6)]

sorted_list = sorted(_list, key = lambda dt: (dt[0], dt[1]))
print(sorted_list)