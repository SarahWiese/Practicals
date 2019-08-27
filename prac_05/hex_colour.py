"""Program to look up hexadecimal colour codes."""
HEX_COLOURS = {"red1": "#ff0000", "purple": "#9020f0", "SpringGreen2": "#00ee76", "turquoise1": "#00f5ff", "yellow1": "#ffff00", "orchid1": "#ff83fa", "DeepSkyBlue1": "#00bfff", "chocolate1": "#ff7f24", "black": "#000000", "white": "#ffffff"}


def main ():
    """Program to return hexadecimal colour codes when colour name is entered."""
    colour = str(input("Enter colour name: "))
    while not is_colour_name_valid(colour):
        colour = str(input("Enter colour name:"))
    else:
        quit()


def is_colour_name_valid(colour):
    """Function to check colour name is in HEX_COLOURS dictionary."""
    if colour in HEX_COLOURS.keys():
        return print((HEX_COLOURS[colour]))
    if colour not in HEX_COLOURS.keys():
        return print("Invalid name!")
    else:
        return False


main()


