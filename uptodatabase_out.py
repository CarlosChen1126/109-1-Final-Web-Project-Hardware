import pymongo
from pymongo import MongoClient
import numpy as np
from gtts import gTTS
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URL=os.getenv("MONGO_URL")
print(MONGO_URL)


def pushup(idd,time):
    
    cluster=MongoClient()
    db=cluster["109-1-web-programming"]
    collection=db["access"]
    collection_online=db["online"]

    print(collection.find().next())
    post={"stdID":idd, "time":time, "direction":"out"}
    collection.insert(post)
    delete={"stdID":idd}
    collection_online.delete_one(delete)

def verify(idd):
    cluster=MongoClient("mongodb+srv://web-programming:WebProgrammingForFinalProject@access-control-system.ce7oy.mongodb.net/109-1-web-programming?retryWrites=true&w=majority")
    db=cluster["109-1-web-programming"]
    collection=db["access"]
    collection_register=db["Register"]
    collection_online=db["online"]
    if(collection_register.find({"stdID":idd}).count()==0):
        speech_text="請先註冊喔咩噗"
        output=gTTS(text=speech_text, lang='zh-tw', slow=False)
        output.save('exitfailr.mp3')
        os.system('mpg321 exitfailr.mp3')
        return False
    else:
        if(collection_online.find({"stdID":idd}).count()==0):
            speech_text="你剛剛沒有刷入喔"
            output=gTTS(text=speech_text, lang='zh-tw', slow=False)
            output.save('exitfailn.mp3')
            os.system('mpg321 exitfailn.mp3')
            return False
        else:
            speech_text="謝謝光臨"
            output=gTTS(text=speech_text, lang='zh-tw', slow=False)
            output.save('exit.mp3')
            os.system('mpg321 exit.mp3')
            return True
