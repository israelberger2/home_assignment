from task import Task

class InvalidId(Exception):
    pass


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.id = 0

    def add_task(self, description, date, status):
        task = Task(description, self.id, date, status)
        self.id += 1
        self.tasks[self.id] = task

        return self.id

   
    def edit_task_description(self, task_id, new_description):
        try:
            self.tasks[task_id].set_description(new_description)
        except:
            raise InvalidId(f"Task with ID {task_id} does not exist.")
             
    
    def edit_task_status(self, task_id, new_status):
        try:
            self.tasks[task_id].set_status(new_status)
        except:
            raise InvalidId(f"Task with ID {task_id} does not exist.")
    

    def remove_task(self, task_id):
        try:
            del self.tasks[task_id]
        except:
            raise InvalidId(f"Task with ID {task_id} does not exist.")
        
    def view_task(self, task_id):
            if task_id not in self.tasks:
                raise InvalidId(f"Task with ID {task_id} does not exist.")
            task = self.tasks[task_id]
            return f"Description: {task.description}, date: {task.date} Status: {task.status}"
            

    

