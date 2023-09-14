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

