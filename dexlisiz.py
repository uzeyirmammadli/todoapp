import psycopg2

class Task:
    def __init__(self, id, title, description, priority=None, due_date = None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def __str__(self) -> str:
        return f'Title -> {self.title}\nDescription -> {self.description}\nPriority -> {self.priority}\nDue_date -> {self.due_date}'
    

def convert_records(db_records):
    tasks = list()
    for r in db_records:
        tasks.append(Task(r[0], r[1], r[2], priority=r[3], due_date=r[4]))
    
    return tasks

# connection string format -> "host=<hostname/address> port=5432 dbname=<database name> user=<username> password=<password>"
conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=todoapp user=todoapp password=1234")

curs = conn.cursor()

curs.execute("SELECT * from tasks")

records = curs.fetchall()

tasks = convert_records(records)
for task in tasks:
    print(task)

