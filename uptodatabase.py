import pymongo
from pymongo import MongoClient
import numpy as np
from gtts import gTTS
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URL=os.getenv("MONGO_URL")
dbNAME=os.getenv("dbNAME")
collection1=os.getenv("collection1")
collection2=os.getenv("collection2")
collection3=os.getenv("collection3")
print(MONGO_URL)

def pushup(idd,time,message):
    
    cluster=MongoClient(MONGO_URL)
    db=cluster[dbNAME]
    collection=db[collection1]
    collection_online=db[collection2]
    post={"stdID":idd, "time":time, "purpose":message, "direction":"in"}
    collection.insert(post)
    post_online={"stdID":idd, "EntryTime":time, "Purpose":message}
    collection_online.insert(post_online)
    print("歡迎進入makerspace")
    speech_text1="歡迎進入"
    speech_text2="makerspace"
    output1=gTTS(text=speech_text1, lang='zh-tw', slow=False)
    output1.save("accessin.mp3")
    output2=gTTS(text=speech_text2, lang='en', slow=False)
    output2.save("makerspace.mp3")
    os.system('mpg321 accessin.mp3')
    os.system('mpg321 makerspace.mp3')

    # ifExist=collection.find({"stdID":idd}).count()
    # print(ifExist)
    # if ifExist>0:
    #     timee=collection.find({"stdID":idd})
    #     timeee=timee[0]["time"]
    #     timeeee=np.array(timeee)
    #     k=np.array(time)
    #     ans=np.append(timeeee,k)
    #     collection.update({"_id":timee[0]["_id"]},{"stdID":idd,"time":ans.tolist()})
    # else:
    #     post={"stdID":idd, "time":time}
    #     collection.insert_one(post)
    print(collection.find().next())
def verify(idd):
    cluster=MongoClient(MONGO_URL)
    db=cluster[dbNAME]
    collection=db[collection1]
    collection_online=db[collection2]
    collection_register=db[collection3]
    if(collection_register.find({"stdID":idd}).count()>0):
        return True
    else:
        return False
def verifyy(idd):
    cluster=MongoClient(MONGO_URL)
    db=cluster[dbNAME]
    collection=db[collection1]
    collection_online=db[collection2]
    if(collection_online.find({"stdID":idd}).count()>0):
        return False
    else:
        return True
