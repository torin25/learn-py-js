for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# using list comprehension
pattern = ["".join(str(j) for j in range(1,i+1)) for i in range(5,0,-1)]

for pat in pattern:
    print(pat)