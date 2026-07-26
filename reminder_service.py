from datetime import datetime

def check_reminders():

    due_date = datetime.strptime(
        "2026-02-01",
        "%Y-%m-%d"
    ).date()

    today = datetime.today().date()

    delay = (today - due_date).days

    if today > due_date:

        print("Send Email Reminder")

        if delay > 2:
            print("Send WhatsApp Reminder")

        if delay > 5:
            print("Trigger IVR Call")