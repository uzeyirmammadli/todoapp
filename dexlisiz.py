import psycopg2

class Task:
    def __init__(self, id, title, description=None):
        self.id = id
        self.title = title
        self.description = description

    def __str__(self) -> str:
        return f'Title -> {self.title}\nDescription -> {self.description}\n'
    

def convert_records(db_records):
    tasks = list()
    for r in db_records:
        tasks.append(Task(r[0], r[1], description=r[2]))
    
    return tasks

# connection string format -> "host=<hostname/address> port=5432 dbname=<database name> user=<username> password=<password>"
try:
    conn = psycopg2.connect("host=localhost port=5432 dbname=taskdb user=taskuser password=mysecretpassword")
except:
    print("Connection error")

curs = conn.cursor()

curs.execute("SELECT * from tasks")

records = curs.fetchall()

tasks = convert_records(records)
for task in tasks:
    print(task)
