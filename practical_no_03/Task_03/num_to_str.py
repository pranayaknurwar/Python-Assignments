n=int(input("Enter the nth number: "))

if 1<=n<=150:
    for i in range(1,n+1):
        print(f"{i}",end="")
else:
    print("Enter the number in range of 1 to 150.")