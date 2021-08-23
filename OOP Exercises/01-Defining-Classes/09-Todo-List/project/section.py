from project.task import Task


class Section:
    tasks = []

    def __init__(self, name):
        self.name = name

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not found task with the name {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                amount_of_removed_tasks += 1

        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        tasks_details = ""
        for task in self.tasks:
            tasks_details += task.details() + "\n"
        return f"Section {self.name} \n" \
               f"{tasks_details}"
