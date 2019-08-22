# Lindsay. I struggled with this section despite re-watching the lecture videos and reading the programming pattern examples on github.
# I was able to write lines 5-8 and i'd played round with the range function with some success but i didn't know line 11.
# After spending several hours and putting a message on the cp1404 slack channel i looked at the solution to get an idea how this sort of program should look.
# I then did the extension work so i could practice this kind of program more. For the below program i produced lines 7-10 and line 12 on my own.

total = 0
n = int(input("Number of items: "))
while n < 0:
    print("Invalid number of items!")
    n = int(input("Number of items: "))
for i in range(n):
    Price = float(input("Price of item: "))
    total += Price
if total > 100:
    total *= 0.9
print("Total price for", n, "items is $ {:.2f}".format(total))




