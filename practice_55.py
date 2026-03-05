n = int(input("enter number : "))
i= 1
fact=1
for i in range(1,n+1):
    fact = fact*i
    i+=1
print("factorial is ",fact)