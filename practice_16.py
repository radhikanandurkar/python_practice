# Find greatest of three numbers.
a = int(input("enter number : "))
b = int(input("enter number : "))
c = int(input("enter number : "))
if a>b and a>c:
    print("greatest number is",a)
elif b>a and b>c:
    print("greatest number is",b)
else:
    print("greatest number is",c)