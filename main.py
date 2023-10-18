from tasks import command
from tasks.container import TaskContainer
from tasks.ports.command import Commander
from tasks.ports.errors import (
    QuitCommandRequest,
    RequestValidationError,
    CommandNotSupported,
)

# tasks = list()
# tasks = TaskContainer()

commander = Commander()


def main():
    print("App is started")
    while True:
        try:
            commander.route()
        except QuitCommandRequest:
            break
        except RequestValidationError as re:
            print(f"request error: {str(re)}")
        except CommandNotSupported as ce:
            print(f"command error: {str(ce)}")

        # if cmd_name == "quit":
        #     break
        # command.process_command(cmd_name, tasks)


if __name__ == "__main__":
    main()
