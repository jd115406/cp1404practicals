from prac_07.project import Project
from datetime import datetime
MENU =  "(L)oad projects\n" \
        "(S)ave projects\n" \
        "(D)isplay projects\n" \
        "(F)ilter projects by date\n" \
        "(A)dd new project\n" \
        "(U)pdate project\n" \
        "(Q)uit"

FILENAME = 'projects.txt'

def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            load_projects()
            print("Project loaded")
        elif choice == 'S':
            pass
        elif choice == 'D':
            pass
        elif choice == 'F':
            pass
        elif choice == 'A':
            pass
        elif choice == 'U':
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    print('Goodbye')

def load_projects():
    """Reads .txt file and return class attributes for each project"""
    project_list = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()  # Skips header line
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = float(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            project_list.append(project)
        return project_list