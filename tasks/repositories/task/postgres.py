import psycopg2
from tasks.domain.models import Task

"""
def convert_records(db_records):
    tasks = list()
    for r in db_records:
        tasks.append(Task(r[0], r[1], r[2], priority=r[3], due_date=r[4]))
    
    return tasks
"""


class TaskPostgresRepository:
    def __init__(self):
        self.db_conn_str = (
            "host=127.0.0.1 port=5432 dbname=todoapp user=todoapp password=1234"
        )
        self.db_client = psycopg2.connect(self.db_conn_str)

    def list(self):
        cursor = self.db_client.cursor()
        cursor.execute("SELECT * FROM tasks;")
        records = cursor.fetchall()

        collection = list()

        for task_rec in records:
            task = Task(task_rec[1], task_rec[2])
            task.priority = task_rec[3]
            task.due_date = task_rec[4]

        for t in collection:
            print(t)

    def add(self, new_task):
        """
        Use database client and execute INSERT query
        to add the new task to the database.
        """
        pass

    def filter(self, search_term):
        """
        Use database client and execute SELECT query
        with WHERE clause on title field to filter
        matching tasks
        """
        pass
