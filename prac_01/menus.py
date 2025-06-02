MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter Name: ")
print(MENU)
choice = input("Enter Choice: ")
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Enter Choice: ")
print("Finished.")