#Python program to read prices of 5 items in a list and then display sum

price =[]
for i in range(1,6):
    number= int(input("enter price of item : "))
    price.append(number)
total=0
product =1
for i in price:
    total +=i
    product *= i
    average = total/len(price)
print(total)
print(product)
print(average)
