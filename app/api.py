from datetime import datetime

import pytz
from fastapi import FastAPI
from firebase_admin import messaging

from controller.habit import getHabitsReminderTrue
from controller.notification import sendNotif, sendReminder

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/send_notification")
def send_notification():
    docs = getHabitsReminderTrue()
    for doc in docs:
        currentTime = datetime.now(pytz.timezone(doc.to_dict()["reminder"]["timezone"]))
        if sendReminder(currentTime=currentTime, habit=doc.to_dict()) is True:
            sendNotif(doc.to_dict())


@app.post("/test_send_firebase_notif")
def test_send_firebase_notif():
    message = messaging.Message(
        notification=messaging.Notification(title="test", body="something wicked"),
        token="cy5dZZqKtXi8JDHD7sk2s4:APA91bHigcp9kTAdYG3xPGai0vk_E65N-olrH_bgof89pc7js9qeUoz4wE7EoPLorJaDuPlOSAlJ8YBJw8vY-YOswHDu6agzeCLhvivL1Mo_Ua-pzVf1KsKmygCcFdsm6JgOInoaybEv",
    )
    response = messaging.send(message)
    # Response is a message ID string.
    print("Successfully sent message:", response)
