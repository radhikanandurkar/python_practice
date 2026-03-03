# Factorial of a number.
i = 1
n = int(input("enter value of n : "))
factorial = 1
for i in range(1,n+1):
    factorial*=i
print(factorial)