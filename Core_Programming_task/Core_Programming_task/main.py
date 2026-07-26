from datetime import datetime


class Stage:
    def __init__(self, stage_name, status="Pending"):
        self.stage_name = stage_name
        self.status = status


class Task:
    def __init__(self, task_id, lesson_name, assigned_to, due_date, task_status):
        self.task_id = task_id
        self.lesson_name = lesson_name
        self.assigned_to = assigned_to
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.task_status = task_status

        self.stages = [
            Stage("AI Image Creation"),
            Stage("Image Voice-over"),
            Stage("Screen Recording"),
            Stage("Screen Recording Voice-over"),
            Stage("Video Editing")
        ]

    def check_task_status(self):
        today = datetime.today()

        if self.task_status == "Completed":
            print(f"Task {self.task_id} is completed.")
            return

        if today > self.due_date:
            overdue_days = (today - self.due_date).days

            print(f"\nTask {self.task_id} is overdue by {overdue_days} days.")
            print("Send Email Reminder")

            if overdue_days > 2:
                print("Send WhatsApp Reminder")

            if overdue_days > 5:
                print("Trigger IVR Call")

        else:
            print(f"\nTask {self.task_id} is on time. No reminder needed.")


task1 = Task(
    task_id=101,
    lesson_name="Introduction to AI",
    assigned_to="Student A",
    due_date="2026-06-04",
    task_status="Completed"
)

task1.check_task_status()

task2 = [
    Task(102, "Introduction to AI", "Student A", "2026-06-01", "Pending"),
    Task(103, "Machine Learning Basics", "Student B", "2026-06-15", "Pending"),
    Task(104, "Deep Learning", "Student C", "2026-06-10", "Completed")
]

for task in task2:
    task.check_task_status()