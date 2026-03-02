# Find profit or loss.
cost_prize = int(input("enter cost prize : "))
selling_prize = int(input("enter selling prize : "))
if selling_prize > cost_prize:
    print("profit of",selling_prize -cost_prize,"rupees")
elif cost_prize > selling_prize:
    print("loss of",cost_prize - selling_prize,"rupees")
elif cost_prize == selling_prize:
    print("no profit ,no loss")
else:
    print("invalid amount")