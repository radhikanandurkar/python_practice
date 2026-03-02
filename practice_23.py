# Find smallest of 3 numbers.
a = int(input("enter number : "))
b = int(input("enter number : "))
c = int(input("enter number : "))
if b>a and c>a:
    print("a is smallest number")
elif a>b and c>b:
    print("b is smallest number")
else:
    print("c is smallest number")