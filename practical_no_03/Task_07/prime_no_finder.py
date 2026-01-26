while True:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    
    if start > 1 and end > start:
        break
    else:
        print("Invalid input! Start must be > 1 and end must be greater than start.")

print("\nPrime numbers between", start, "and", end, "are:")


for num in range(start, end + 1):
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)