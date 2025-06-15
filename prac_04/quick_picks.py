"""
CP1404 - Practical
Quick picks
"""
import random

NUMBER_OF_LINES = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBER_OF_LINES):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()
