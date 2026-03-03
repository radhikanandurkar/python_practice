# Check palindrome number.
n = int(input("enter number : "))
reverse = 0
original = n
while n!=0:
    last_digit = n%10
    reverse = reverse *10 + last_digit
    n= n//10

if original==reverse:
    print("number is palindrome")
else:
    print("number is not palindrome")