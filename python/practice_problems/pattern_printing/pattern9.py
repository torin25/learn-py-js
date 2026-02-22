char="*"
space=" "
n=5
# upper triangle
for i in range(1,6):
    print(space*(n-i),end="")
    for j in range(1,i+1):
        print(char,end='')
    for j in range(i-1,0,-1):
        print(char,end='')
    print(space*(n-i))
        

# lower trinagle
for i in range(5,0,-1):
    print(space*(n-i),end="")
    for j in range(1,i+1):
        print(char,end="")
    for j in range(i-1,0,-1):
        print(char, end="")
    print(space*(n-i))