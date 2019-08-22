# 1.	When will a ValueError occur?
#When the users enters non integer value for numerator or denominator. e.g “a”
# 2.	When will a ZeroDivisionError occur?
# When the user enters 0 for the denominator value.
# 3.	Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes.
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Denominator cannot be Zero: ")
            denominator = int(input("Enter non Zero denominator: "))
        else:
            fraction = numerator / denominator
            valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print(fraction)
print("Finished.")
