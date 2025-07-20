from prac_07 import project
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
    projects = []
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            projects = load_projects(FILENAME)
            print("Project loaded")
        elif choice == 'S':
            pass
        elif choice == 'D':
            display_projects(projects)
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

def load_projects(FILENAME):
    """Reads .txt file and return class attributes for each project"""
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()  # Skips header line
        for line in in_file:
            parts = line.strip().split('\t')
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = float(parts[4])
            project = Project(parts[0], parts[1], priority, cost_estimate, completion_percentage)
            projects.append(project)
        return projects

def display_projects(projects):
    """Displays completed and incomplete projects"""
    completed_projects = sorted([project for project in projects if project.completion_percentage == 100])
    incomplete_projects = sorted([project for project in projects if project.completion_percentage < 100])

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

def filter_projects(projects):
    start_date = input("Display projects that start after date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
    filtered_projects = sorted([project for project in projects if project.start_date >= start_date])

    for project in filtered_projects:
        print(project)

def add_project(projects):
    print("To add a new project input the following details:")
    name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = float(input("Completion percentage: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

if __name__ == '__main__':
    main()