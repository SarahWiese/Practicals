"""Program to generate chosen number of Quick Pick lottery numbers"""
import random
quick_picks = []
number_of_quick_picks = int(input("How many quick picks?"))

for number_of_quick_pick in range(1, number_of_quick_picks + 1):
    quick_pick = [random.randint(1, 45) for i in range(6)]
    quick_pick.sort()
    quick_picks.append(quick_pick)
for ticket in quick_picks:
    print(*ticket)
