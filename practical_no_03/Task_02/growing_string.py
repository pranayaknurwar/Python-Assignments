s = "Python"

for i in range(1, len(s) + 1):
    for ch in s[:i]:
        print(ch,end=" ")
    print("\n")
