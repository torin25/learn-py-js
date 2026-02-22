n=5
spaces=" "
char="*"

for i in range(1,6):
    for j in range(1,i+1):
        print(char,end="")
    print(spaces*(n-i))

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(char,end="")
    print(spaces*(n-i))   
