import unittest
import io
import sys
from datetime import datetime
from unittest.mock import patch

from tasks.ports.command import Commander, CommandAddRequest
from tasks.ports.errors import (
    CommandNotSupported,
    RequestValidationError,
    QuitCommandRequest
)


class TestCommander(unittest.TestCase):
    stdin = sys.stdin
    add_data = "\n".join(["Mocked Task title", "Mocked Task descriptio", "", ""])
    mock_stdin = patch("std.stdin", new_callable=io.StringIO(add_data))
    sys.stdin = mock_stdin

    def tearDown(self):
        sys.stdin = self.stdin

    def test_commander_init(self):
        commander = Commander()
        self.assertEqual(None, commander.cmd_type)

    def test_valid_command_type(self):
        commander = Commander()
        commander.cmd_type = "add"
        self.assertEqual("add", commander.cmd_type)
    
    def test_invalid_command_type(self):
        commander = Commander()

        with self.assertRaises(CommandNotSupported):
            commander.cmd_type = "invalid_command"
            self.assertNotEqual("invalid_command", commander.cmd_type)
    
    def test_handle_quit(self):
        commander = Commander()
        with self.assertRaises(QuitCommandRequest):
            commander.handle_quit()
    
    def test_handle_add_default(self):
        commander = Commander()

        try:
            commander.handle_add()
        except Exception as e:
            self.fail(str(e))




class TestCommandAddRequest(unittest.TestCase):
    def test_default_add_request(self):
        task_title = "test task title" 
        task_description = "test task description"
        add_request = CommandAddRequest(task_title, task_description)

        self.assertEqual(task_title, add_request.title)
        self.assertEqual(task_description, add_request.description)
    
    def test_default_add_request_validation(self):
        task_title = "test task title" 
        task_description = "test task description"
        add_request = CommandAddRequest(task_title, task_description)

        try:
            add_request.validate()
        except RequestValidationError as e:
            self.fail(e)
    
    def test_valid_initial_priority(self):
        # set input data and expected values
        expected_priority = "2"
        input_data = {
            "title": "test task title",
            "description": "test task description",
            "priority": expected_priority
        }
        
        # create request object
        add_request = CommandAddRequest(**input_data)

        # assert
        self.assertEqual(expected_priority, add_request.priority)
            
    def test_valid_priority_validation(self):
        # set input data and expected values
        input_data = {
            "title": "test task title",
            "description": "test task description",
            "priority": "2"
        }
        expected_priority = 2
        
        # create request object
        add_request = CommandAddRequest(**input_data)

        try:
            validated_data = add_request.validate()
        except RequestValidationError as e:
            self.fail(e)

        self.assertEqual(expected_priority, validated_data["priority"])
    
    def test_invalid_priority_validation(self):
        # set input data and expected values
        input_data = {
            "title": "test task title",
            "description": "test task description",
            "priority": "iu"
        }

         # create request object
        add_request = CommandAddRequest(**input_data)

        with self.assertRaises(RequestValidationError):
            add_request.validate()

    def test_valid_due_date_validation(self):
        # set input data and expected values
        input_data = {
            "title": "test task title",
            "description": "test task description",
            "due_date": "11-Jan-2023"
        }
        # expected_due_date = datetime.strptime("11-Jan-2023", '%d-%b-%Y')
        expected_due_date = datetime.strptime(input_data["due_date"], '%d-%b-%Y')

        # create request object
        add_request = CommandAddRequest(**input_data)

        try:
            validated_data = add_request.validate()
        except RequestValidationError as e:
            self.fail(e)

        self.assertEqual(expected_due_date, validated_data["due_date"])

    def test_invalid_due_date_validation(self):
        # set input data and expected values
        input_data = {
            "title": "test task title",
            "description": "test task description",
            "due_date": "HHJHJHJ"
        }

        # create request object
        add_request = CommandAddRequest(**input_data)

        with self.assertRaises(RequestValidationError):
            add_request.validate()