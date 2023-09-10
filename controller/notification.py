from datetime import datetime

from config import db


def sendReminder(currentTime: datetime, habit: dict):
    if "isDone" in habit:
        if habit["isDone"] == True:
            return False
    currentHour = currentTime.hour
    currentMinute = currentTime.minute
    reminderHour = int(habit["reminder"]["secondSinceMidnight"] / 3600)
    reminderMinute = int((habit["reminder"]["secondSinceMidnight"] % 3600) / 60)
    if reminderHour == currentHour and reminderMinute == currentMinute:
        return True
    return False


def sendNotif(habit: dict):
    db.collection("notifications").add(
        {
            "userId": habit["userId"],
            "createTime": datetime.utcnow(),
            "habitName": habit["name"],
            "isRead": False,
        }
    )
