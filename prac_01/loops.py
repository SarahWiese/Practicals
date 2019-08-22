# count in 10s from 0 to 100
for i in range(1, 21, 2):
    print(i, end=' ')
print()
# count down from 20 to 1
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# Print n stars
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# Print n lines of increasing stars
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    s = "*"
    print(s, end=' ')
number_of_stars = int(input("Enter number of stars: "))
for i in range(1, number_of_stars + 1):
    s = "*"
    print(i * s)
# sales bonus with loop
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
        print("Bonus ${:.2f}".format(bonus))
        sales = float(input("Enter sales: $"))
    elif sales >= 1000:
        bonus = sales * 0.15
        print("Bonus ${:.2f}".format(bonus))
        sales = float(input("Enter sales: $"))
else:
    print("Zero Bonus")
