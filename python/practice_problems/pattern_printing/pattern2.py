char = "*"
for i in range(1,6):
    print(char*i)


# using list comprehension
pattern_list = [char*i for i in range(1,6)]
for pattern in pattern_list:
    print(pattern)