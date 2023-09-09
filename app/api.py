from datetime import datetime

import pytz
from fastapi import FastAPI

from controller.habit import getHabitsReminderTrue
from controller.notification import sendNotif, sendReminder

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/send_notification")
def get_data():
    docs = getHabitsReminderTrue()
    for doc in docs:
        currentTime = datetime.now(pytz.timezone(doc.to_dict()["reminder"]["timezone"]))
        if sendReminder(currentTime=currentTime, habit=doc.to_dict()) is True:
            sendNotif(doc.to_dict())
