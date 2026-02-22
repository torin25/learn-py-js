# for i in range(1,6):
#     print(str(i)*i)


# using plain string joining method
print("\n".join(str(i)*i for i in range(1,6)))

# using list comprehension
pattern = [str(i)*i for i in range(1,6)]
for pat in pattern:
    print(pat)