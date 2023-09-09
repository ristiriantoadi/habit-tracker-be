from datetime import datetime

from fastapi import FastAPI

from config import db

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create")
def create():
    db.collection("persons").add({"name": "somebody", "createTime": datetime.utcnow()})


@app.post("/send_notification")
def get_data():
    docs = db.collection("habits").get()
    for doc in docs:
        print((doc.to_dict()["name"]))
        print((doc.to_dict()["createTime"].year))
        print("")
