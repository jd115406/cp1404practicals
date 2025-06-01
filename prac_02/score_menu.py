"""
CP1404 - Score menu
"""

def main():
    """Main menu handles all user input"""
    score = int(input("Score: "))
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(print_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Goodbye")


def get_valid_score():
    """Get a valid score between 0-100"""
    score = int(input("Score:"))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score:"))
    return score


def print_result(score):
    """Print the corresponding grade based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Good"
    else:
        return "Bad"


def show_stars(score):
    """Print star length corresponding to score"""
    print("*" * score)

main()
