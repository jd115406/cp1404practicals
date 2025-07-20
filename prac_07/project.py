from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize project object"""
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String representation of Project class"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}. priority: {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Sort projects by priority"""
        return self.priority < other.priority