import datetime

class Task:
    def __init__(self, title, description, priority=4, due_date = None):
        self.title = title
        self.description = description

        # we assume default value of priority as the lowest
        # so it's known, not a None, and 4 as of now
        self._priority = priority
        self._due_date = due_date
    
    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, p):
        self._priority = p

    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, dd):
        self._due_date = dd

    def __str__(self):
        return """
        title: \"{}\" is {} with due date {}
            {}
        """.format(self.title, self.priority, self.due_date, self.description)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": None if self.due_date is None else self.due_date.strftime("%d-%b-%Y")
        }
