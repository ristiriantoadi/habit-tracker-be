from config import db


def getHabitsReminderTrue():
    return db.collection("habits").where("reminder.send", "==", True).get()
