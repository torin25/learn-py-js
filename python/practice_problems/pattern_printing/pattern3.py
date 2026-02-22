for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


# using plain string join method
for i in range(1,6):
    print("".join(str(i) for i in range(1,i+1))) #generator
    # print("".join([str(i) for i in range(1,i+1)])) #list

# using list comprehension
for i in range(1,6):
    pattern = [str(j) for j in range(1,i+1)]
    print("".join(pattern))