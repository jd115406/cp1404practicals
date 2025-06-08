#Question 1:
user_name = input("Name: ")
out_file = open('data.txt', "w")
print(user_name, file=out_file)
out_file.close()

#Question 2:
out_file = open('data.txt', "r")
print("Hello!", out_file.read())
out_file.close()

#Question 3:
with open("numbers.txt", "r") as file:
    number_1 = int(file.readline())
    number_2 = int(file.readline())
    print(number_1 + number_2)

#Question 4:
total = 0
with open("numbers.txt", "r") as file:
    try:
        for line in file:
            total += int(line)
    except ValueError:
        print("Invalid file, ensure all lines are integers!")
print(total)

















