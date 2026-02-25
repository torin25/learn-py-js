# def count_digits_one(num):
#     if num>=0 and num<=9:
#         return 1
#     count=0
#     while True:
#         rem = num%10
#         num=(num-rem)//10
#         count+=1
#         if num==0:
#             break
#     return count

def count_digits(num):
    if num>=0 and num<=9:
        return 1
    count=0
    while num>0:
        num=num//10
        count+=1
    return count

def main():
    while True:
        try:
            num = int(input("Enter an integer: "))
            break
        except ValueError:
            print("\nInvalid input, please try again.\n")

    num=abs(num)
    print(f"The number of digits in {num} is : {count_digits(num)}")
if __name__ == "__main__":
    main()