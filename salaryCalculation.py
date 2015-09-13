payRate = 10.0
standardWorkTime = 160.0
workTime = float(input("Enter the work time: "))
if workTime > standardWorkTime:
    grossPay = standardWorkTime * payRate + (workTime - standardWorkTime) * payRate * 1.5
else:
    grossPay = workTime * payRate
print("Gross Pay = ", grossPay)
if grossPay >= 1500:
    tax = 1000 * 0.1 + 500 * 0.2 + (grossPay - 1500) * 0.3
elif grossPay >= 1000:
    tax = 1000 * 0.1 + (grossPay - 1000) * 0.3
else:
    tax = grossPay * 0.1
print("Taxes = ", tax)
netPay = grossPay - tax
print("Net pay = ", netPay)
