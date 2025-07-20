from prac_07 import project
from prac_07.project import Project
from datetime import datetime

MENU = "(L)oad projects\n" \
       "(S)ave projects\n" \
       "(D)isplay projects\n" \
       "(F)ilter projects by date\n" \
       "(A)dd new project\n" \
       "(U)pdate project\n" \
       "(Q)uit"

FILENAME = 'projects.txt'


def main():
    """Print main-menu and facilitate user input to call desired function"""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            projects = load_projects(FILENAME)
            print("Project loaded")
        elif choice == 'S':
            save_projects(projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
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
    """Filters projects by projects after the user specified date"""
    start_date = input("Display projects that start after date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
    filtered_projects = sorted([project for project in projects if project.start_date >= start_date])

    for project in filtered_projects:
        print(project)


def add_project(projects):
    """Add project to the projects list through user input"""
    print("Let's add a new project:")
    name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = float(input("Completion percentage: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Updates projects based on user input"""
    for i, project in enumerate(projects):
        print(f"{i}. {project}")
    update_choice = int(input("Project choice: "))
    selected_project = projects[update_choice]
    print(f"Selected project: {selected_project}")

    new_percentage = int(input("New percentage: "))
    while new_percentage < 0 or new_percentage > 100:
        print(f"Invalid percentage {new_percentage}, does not lie within 0 and 100")
        new_percentage = int(input("New percentage: "))
        selected_project.completion_percentage = new_percentage

        new_priority = int(input("New priority: "))
        selected_project.priority = new_priority


def save_projects(projects):
    """Write projects data to a file"""
    with open(FILENAME, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}",
                file=out_file)


if __name__ == '__main__':
    main()
