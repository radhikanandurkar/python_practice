# Check character is vowel or consonant.
a = "aeiou"
char = input("enter character : ")
if char.isalpha():
    if char.lower() in a:
        print("enter character is vowel")
    else:
        print("enter charecter is consonant")
else:
    print("not alphabet")