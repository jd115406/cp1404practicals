from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My Guitars!")
    name = input("Name: ")

    while name != "": #Continue to input until a blank name is entered
        year = int(input("Year: "))
        cost_input = input("Cost: ").replace("$", "")
        cost = float(cost_input)
        new_guitar_input = Guitar(name, year, cost)
        guitars.append(new_guitar_input)
        print(f"{new_guitar_input} added")
        name = input("Name: ")

    if guitars: #If there are items in the list
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)" #ensures that vintage guitars are labelled
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars added")

if __name__ == "__main__":
    main()
