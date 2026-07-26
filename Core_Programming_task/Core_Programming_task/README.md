# Mini Task Tracker with Reminder Logic (Demo Level) 

## Explanation:

The program uses a Task class to store task details such as Task ID, Lesson Name, Assigned Creator, Due Date, and Task Status. Each task contains five predefined workflow stages with their own status. The system compares the current date with the task's due date. If the task is not completed and the due date has passed, it is considered overdue. An Email Reminder is printed for all overdue tasks. If the task is overdue by more than 2 days, a WhatsApp Reminder is printed, and if overdue by more than 5 days, an IVR Call is triggered. If the task is completed or not yet due, no reminder is sent.

## Assumptions:

- A task marked as Completed does not require any reminders.
- The due date is provided in YYYY-MM-DD format.
- Reminder actions are simulated using print statements only; no actual email, WhatsApp, or IVR integration is implemented.
- All tasks follow the same fixed workflow stages.