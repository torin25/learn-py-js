def collatz_sequence(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
    
def main():
    while True:
        try:
            n=int(input("Enter a positive integer: "))
            if n<=0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    sequence=[n]
    while n!=1:
        n=collatz_sequence(n)
        sequence.append(n)
    
    for num in sequence:
        print(num)


if __name__ == "__main__":
    main()



                    