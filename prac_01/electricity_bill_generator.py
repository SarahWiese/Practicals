# Electricity bill estimator
print("Electricity bill generator")
total = 0
cents = int(input("Enter cents per kwh: "))
daily_use = float(input("Enter daily use in kwh: "))
billing_days = int(input("Enter number of billing days: "))
total += (cents/100) * daily_use * billing_days
print("Estimated bill: ${:.2f} ".format(total))

# Electricity bill estimator 2.0
print("Electricity bill generator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
total = 0
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kwh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff == 11:
    total += TARIFF_11 * daily_use * billing_days
    print("Estimated bill: ${:.2f} ".format(total))
else:
    total += TARIFF_31 * daily_use * billing_days
    print("Estimated bill: ${:.2f} ".format(total))
