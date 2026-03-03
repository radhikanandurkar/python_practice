# sum of digit
num = int(input("enter number : "))
sum = 0
while num!=0:
    number = num%10
    sum = sum + number
    num = num//10
print(sum)