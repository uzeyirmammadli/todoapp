import unittest
from datetime import datetime
from tasks.task import Task, TaskValueError

class TestTask(unittest.TestCase):
    def test_default_task_values(self):
        title = "Test title"
        description = "Test description"

        task = Task(title=title, description=description)
        
        self.assertEqual(title, task.title)
        self.assertEqual(description, task.description)

    def test_valid_priority(self):
        task = Task("test_task_title", "test_task_description")
        expected_priority = 2
        
        task.priority = expected_priority
        self.assertEqual(expected_priority, task.priority)
    
    def test_invalid_priority(self):
        task = Task("test_task_title", "test_task_description")
        invalid_priority = 5

        with self.assertRaises(TaskValueError):    
            task.priority = invalid_priority
            self.assertNotEqual(invalid_priority, task.priority)
    
    def test_valid_due_date(self):
        task = Task("test_task_title", "test_task_description")
        expected_due_date = datetime.strptime("23-jan-2023", '%d-%b-%Y')

        task.due_date = expected_due_date
        self.assertEqual(expected_due_date, task.due_date)

    def test_invalid_due_date(self):
        task = Task("test_task_title", "test_task_description")
        invalid_due_date = "23/5/2022"

        with self.assertRaises(TaskValueError): 
            task.due_date = invalid_due_date
            self.assertNotEqual(invalid_due_date, task.due_date)

if __name__ == "__main__":
    unittest.main()