principle=float(input("Enter Principle:"))
rate=float(input("Enter Rate:"))
time=float(input("Enter time:"))
intrest=principle*(1+rate/100)**time-principle
print("The amount of compound interest is",intrest)