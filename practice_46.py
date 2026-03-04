# Find power of number using loop.
base = int(input("enter base  number : "))
power = int(input("enter the power : "))
result = 1
# for i in range(power):
#     result = result*base
# print("answer :",result)


# another method
i = 1
while i<=power:
    result=result*base
    i+=1
print(result)