# Electricity bill calculation.
unit = int(input("enter units : "))
if unit<=100:
    bill = unit*5
elif unit<=300:
    bill = (unit*5)+(unit- 100)*7
else:
    bill = (unit*5)+(300*7) +(unit-300)*10
print(bill)