# check palindrome of word.
word= input("enter word : ")
original = word
reverse =""
for i in word:
    reverse = i+reverse
if original == reverse:
    print("palindrome")
else:
    print("not palindrome")