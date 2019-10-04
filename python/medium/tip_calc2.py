bill = float(input("Total bill amount? "))
service = input("Level of service? ")
party = float(input("Split how many ways? "))

if service == "good":
    tip = float((20/100)*bill)
    print("Tip amount $"+"%.2f" % tip)
    total = bill + tip
    print("Total amount: $"+"%.2f" % total)
    per_pax = total / party
    print("Amount per person: $"+"%.2f" % per_pax)
elif service == "fair":
    tip = float((15/100)*bill)
    print("Tip amount $"+"%.2f" % tip)
    total = bill + tip
    print("Total amount: $"+"%.2f" % total)
    per_pax = total / party
    print("Amount per person: $"+"%.2f" % per_pax)
elif service == "bad":
    tip = float((10/100)*bill)
    print("Tip amount $"+"%.2f" % tip)
    total = bill + tip
    print("Total amount: $"+"%.2f" % total)
    per_pax = total / party
    print("Amount per person: $"+"%.2f" % per_pax)
else:
    print("Please enter good, fair or bad service")
