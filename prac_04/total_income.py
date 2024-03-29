"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of payday."""
    incomes = []
    payday = int(input("How many payday's? "))

    for month in range(1, payday + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_income(incomes, payday)


def print_income(incomes, payday):
    """Function to print income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, payday + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()