import json
from tasks.domain.models import Task


class TaskMemoryRepository:
    def __init__(self):
        self.collection = list()

    def add(self, new_task):
        if isinstance(new_task, Task):
            self.collection.append(new_task)

    def list(self):
        for task in self.collection:
            print(task)

    def filter(self, search_term):
        for task in self.collection:
            if task.title.find(search_term) >= 0:
                print(task)


class TaskJsonRepository:
    def __init__(self):
        self.collection = {"tasks": []}
        self.tasks_file_name = "tasks.json"

        with open(self.tasks_file_name, "r+") as tasks_file:
            file_data = tasks_file.read()
            task_data = json.loads(file_data)
            self.collection["tasks"] = [Task(**task) for task in task_data["tasks"]]

    def add(self, new_task):
        self.collection["tasks"].append(new_task)

        with open(self.tasks_file_name, "r+") as tasks_file:
            tasks_list = {}
            tasks_list["tasks"] = [task.to_dict() for task in self.collection["tasks"]]
            tasks_data = json.dumps(tasks_list)
            tasks_file.write(tasks_data)

    def list(self):
        for task in self.collection["tasks"]:
            print(task)

    def filter(self, search_term):
        for task in self.collection["tasks"]:
            if task.title.find(search_term) >= 0:
                print(task)
