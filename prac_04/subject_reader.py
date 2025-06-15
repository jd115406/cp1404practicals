"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)
        print("----------")
        subject_data.append(parts)
    input_file.close()
    return subject_data


def print_subject_details(subject_data):
    """Print details about each subject."""
    for subject in subject_data:
        subject, lecturer, number_of_students = subject
        print(f"{subject} is taught by {lecturer} with {number_of_students} students.")


main()
