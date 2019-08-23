numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0]
numbers[-1]
numbers[3]
numbers[:1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

# numbers[0]            3
# numbers[-1]           9 /  2
# numbers[3]            1
# numbers[:1]           3, 1, 4, 1, 5, 9, 2     / 3
# numbers[3:4]          1, 2    / 1
# 5 in numbers          1   / True
# 7 in numbers          0   /False
# "3" in numbers        0   / False
# numbers + [6, 5, 3]   3, 1, 4, 1, 5, 9, 2, 6, 5, 3