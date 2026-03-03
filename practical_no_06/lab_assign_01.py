text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    
    if ch == " ":
        spaces += 1
    
    if ch.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)