"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Program to return score."""
    score = float(input("Enter score: "))
    while not is_score_valid(score):
        print("Enter Score: ")
    else:
        print("Invalid Score")


def is_score_valid(score):
    """Function to determine if score is valid and return grade"""
    if 90 <= score <= 100:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return False


main()
