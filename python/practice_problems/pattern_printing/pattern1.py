pattern = "*"*5
for _ in range(5):
    print(pattern)

# using list comprehension
pat = [pattern for _ in range(5)]
for pattern in pat:
    print(pattern)