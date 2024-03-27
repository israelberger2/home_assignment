class Task:
    def __init__(self, description, task_id, date, status):
        self.description = description
        self.task_id = task_id
        self.date = date
        self.status = status

    def set_status(self, new_status):
        self.status = new_status

    def set_description(self, new_description):
        self.description = new_description

    def set_date(self, date):
        self.date = date
        