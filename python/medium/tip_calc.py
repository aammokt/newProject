bill = float(input("Total bill amount? "))
service = input("Level of service? ")
if service == "good":
    tip = float((20/100)*bill)
    print("Tip amount $"+"%.2f" % tip)
    total = bill + tip
    print("Total amount: $"+"%.2f" % total)
elif service == "fair":
    tip = float((15/100)*bill)
    print("Tip amount $"+"%.2f" % tip)
    total = bill + tip
    print("Total amount: $"+"%.2f" % total)
elif service == "bad":
    tip = float((10/100)*bill)
    print("Tip amount $"+"%.2f" % tip)
    total = bill + tip
    print("Total amount: $"+"%.2f" % total)
else:
    print("Please enter good, fair or bad service")