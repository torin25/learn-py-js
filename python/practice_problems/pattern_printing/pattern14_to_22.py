# pattern 14
# chars = ['A','B','C','D','E']
# for i in range(5):
#     for j in range(i+1):
#         print(chars[j],end="")
#     print()

# pattern 15
# chars = ['A','B','C','D','E']
# for i in range(5,0,-1):
#     for j in range(i):
#         print(chars[j],end="")
#     print()

# pattern 16
# chars = ['A','B','C','D','E']
# for i in range(5):
#     print(chars[i]*(i+1))

# pattern 17
# chars = ['A','B','C','D','E']

# n=7
# space=" "
# for i in range(5):
#     print(space*(n-i),end="")

#     for j in range(i+1):
#         print(chars[j],end="")

#     for j in range(i-1,-1,-1):
#         print(chars[j],end="")

#     print(space*(n-i))

# pattern 18

# using extra list to store pattern and apply reverse() function
# chars = ['A','B','C','D','E']
# chars_list=[]
# j=0
# n=len(chars)
# for i in range(5):
#     chars_list.append(chars[j:n])
#     j+=1
# chars_list.reverse()
# for char in chars_list:
#     print(" ".join(char))

# without using extra list
# chars = ['A','B','C','D','E']
# n=len(chars)
# for i in range(n-1,-1,-1):
#     print(" ".join(chars[i:n]))


# pattern 19

# n=5
# space=" "
# char="*"

# # for the upper half of the pattern
# for i in range(5,0,-1):
#     print(char*i,end="")
#     print(space*(n-i)*2,end="")
#     print(char*i)

# # for lower half of the pattern
# for i in range(1,6):
#     print(char*i,end="")
#     print(space*(n-i)*2,end="")
#     print(char*i)


# # pattern 20
# n=5
# space=" "
# char="*"
# # # for upper half of the pattern
# for i in range(1,6):
#     print(char*i,end="")
#     print(space*(n-i)*2,end="")
#     print(char*i)

# # for the upper half of the pattern
# for i in range(4,0,-1):
#     print(char*i,end="")
#     print(space*(n-i)*2,end="")
#     print(char*i)


# # pattern 21
# print * if the position is on the border else print space

# n=4
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()
    

# pattern 22

n=7
num=4
pattern=[[_ for _ in range(n)] for _ in range(n)]
m=0
k=n
while m<n and num>0:
    for i in range(m,k):
        for j in range(m,k):
            if i==m or i==k-1 or j==m or j==k-1:
                pattern[i][j]=num
    m+=1
    k-=1
    num-=1


for i in range(n):
    for j in range(n):
        print(pattern[i][j],end=" ")
    print() 