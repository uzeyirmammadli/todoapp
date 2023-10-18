def process_command(cmd, container):
    if cmd == "add":
        # add_task(container)
        container.add()
    elif cmd == "list":
        # list_tasks(container)
        container.list()
    elif cmd == "filter":
        # filter_tasks(container)
        container.filter()
