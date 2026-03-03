#Count digits in a number.
n =int(input("enter any digit number : "))
count = 0
while n!=0:
    n = n //10
    count+=1
print("total digit",count)