class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title:
            raise ValueError("Task title cannot be empty")
        task = Task(title)
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if index >= len(self.tasks):
            raise IndexError("Task not found")
        self.tasks[index].mark_complete()

    def delete_task(self, index):
        if index >= len(self.tasks):
            raise IndexError("Task not found")
        self.tasks.pop(index)

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.completed]