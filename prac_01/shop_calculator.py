total_cost = 0

number_of_items = int(input("Number of items: "))
while  number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_items = float(input("Price of item: "))
    total_cost = total_cost + price_of_items
    if total_cost > 100:
        total_cost = total_cost * 0.9
print(f"Total price for {number_of_items} items is: {total_cost}")