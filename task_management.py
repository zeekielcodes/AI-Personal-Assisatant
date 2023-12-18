import os
class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = self.read_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.write_tasks()
        print("Task added successfully.")

    def update_task(self, task_index, updated_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = updated_task
            self.write_tasks()
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            self.write_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("\nTasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

    def read_tasks(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write("")
        with open(self.filename, 'r') as file:
            tasks = file.read().splitlines()
        return tasks

    def write_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def task_manager_menu(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. View Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
                task_index = int(input("Enter the task number to update: "))
                updated_task = input("Enter the updated task: ")
                self.update_task(task_index, updated_task)
            elif choice == "3":
                self.view_tasks()
                task_index = int(input("Enter the task number to delete: "))
                self.delete_task(task_index)
            elif choice == "4":
                self.view_tasks()
            elif choice == "5":
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
