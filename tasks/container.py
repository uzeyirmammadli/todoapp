from tasks.task import Task, TaskValueError
from datetime import datetime


class TaskContainer:
    def __init__(self, tasks=[]) -> None:
        self._tasks = tasks

    def add(self):
        print("Add your new task")
        title = input("Task title: ")
        desc = input("Task description: ")
        priority = input("Set task priority: ")
        due_date = input("Set task due_date: ")

        t = Task(title=title, description=desc)

        try:
            t.priority = int(priority)
        except ValueError:
            print("Input value is not integer")
        except TaskValueError as e:
            print("error: ", e)

        try:
            t.due_date = datetime.strptime(due_date, "%d-%b-%Y")
        except TaskValueError as e:
            print("error: ", e)
            # print("error: invalid due date, ", str(due_date), " should be a datetime")

        self._tasks.append(t)

    def list(self):
        for task in self._tasks:
            print(task)

    def filter(self):
        print("Choose your filtering option")
        print("[1] Priority")
        print("[2] Due date")

        try:
            filtering_option = int(input("Option: "))
        except ValueError:
            print("Invalid non-numeric input. Option value must be 1 or 2")
            return

        if filtering_option == 1:
            self._filter_by_priority()
        elif filtering_option == 2:
            print("Not implemented yet")

        else:
            print("Invalid input. Option value must be 1 or 2")
            return

    def _filter_by_priority(self):
        priority = input("Set priority filtering value: ")
        try:
            priority = int(priority)
        except ValueError:
            print("Input value is not integer")

        for task in self._tasks:
            if task.priority == priority:
                print(task)
