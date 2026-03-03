# Product of digits.
num = int(input("enter number : "))
product = 1
while num !=0:
    number = num%10
    product =product*number
    num = num//10
print(product)