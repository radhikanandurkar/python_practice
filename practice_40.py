# Reverse a number.
n = int(input("enter number to reverse : "))
reverse = 0 
while n!=0:
    last_digit = n%10
    reverse = reverse *10 + last_digit
    n= n//10
print(reverse)