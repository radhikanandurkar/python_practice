# WAP to Separate and display even and odd numbers from a list.

number =[]
while True:
    num = input("want to add number ")
    if num =='yes':
        n= int(input("enter number : "))
        number.append(n)
    elif num =='no':
        break
    else:
        print("invalid answer")
even =[]
odd = []
for i in number:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)