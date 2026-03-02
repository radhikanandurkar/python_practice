# Check alphabet, digit, or special character.
char = input("enter a charecter : ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("special charecter")