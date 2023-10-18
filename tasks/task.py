from datetime import datetime


class Task:
    def __init__(self, title, description, priority=4, due_date=None):
        self.title = title
        self.description = description

        # check priority range [1..4]
        if priority >= 1 and priority <= 4:
            self._priority = priority
        else:
            raise TaskValueError(
                "invalid priority -> {} should be in range 1 to 4".format(priority)
            )

        # check due_date to be None of valid datetime
        if due_date is not None:
            if isinstance(due_date, datetime):
                self._due_date = due_date
            else:
                raise TaskValueError(
                    "invalid due_date -> {} should be datetime".format(due_date)
                )
                # print("error: invalid due date, ", str(due_date), " should be a datetime")
        else:
            self._due_date = due_date

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, p):
        if p >= 1 and p <= 4:
            self._priority = p
        else:
            raise TaskValueError(
                "invalid priority -> {} should be in range 1 to 4".format(p)
            )

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, dd):
        # check due_date to be None of valid datetime
        if dd is not None:
            if isinstance(dd, datetime):
                self._due_date = dd
            else:
                raise TaskValueError(
                    "invalid due date -> {} should be a datetime".format(dd)
                )
            # print("error: invalid due date, ", str(dd), " should be a datetime")

    def __str__(self):
        return """
        title: \"{}\" is {} with due date {}
            {}
        """.format(
            self.title, self.priority, self.due_date, self.description
        )


class TaskValueError(Exception):
    pass
