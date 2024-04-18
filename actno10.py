try:
    msg = str(input("Enter your message: "))
except ValueError:
    print("Error: Input is not a valid string.")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in msg:
    if i.lower() in vowels:9
        count += 1

print("Number of vowels:", count)