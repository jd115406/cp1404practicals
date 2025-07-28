from prac_07.guitar import Guitar

guitars = []
FILENAME = 'guitars.csv'

with open(FILENAME, 'r') as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name, year, cost))

    guitar_name = input('Guitar name: ').title()
    while guitar_name != "":
        guitar_year = int(input('Guitar year: '))
        guitar_cost = float(input('Guitar cost: '))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        guitar_name = input('Guitar name: ').title()

    guitars.sort()

    for guitar in guitars:
        print(guitar)



