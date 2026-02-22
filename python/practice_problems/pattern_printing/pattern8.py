char="*"
n=5
space=" "

for i in range(5,0,-1):
    print(space*(n-i),end="")
    for j in range(1,i+1):
        print(char,end="")
    for j in range(i-1,0,-1):
        print(char, end="")
    print(space*(n-i))