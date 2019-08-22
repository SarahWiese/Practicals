"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Program to convert Celsius to Fahrenheit and Fahrenheit to Celsius"""
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            while not convert_celsius_to_fahrenheit():
                print("Result: {:.2f} F".format(convert_celsius_to_fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            while not convert_fahrenheit_to_celsius():
                print("Result: {:.2f} C" .format(convert_fahrenheit_to_celsius))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit():
    """Function to convert Celcius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius():
    """Function to convert Fahrenheit to Celsius"""
    celsius = 5 / 9.0 * (fahrenheit - 32)


main()
