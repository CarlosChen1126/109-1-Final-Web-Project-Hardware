import serial
import time
import json
import uptodatabase
import mictest
from gtts import gTTS
import os


X=True
COM_PORT = "/dev/ttyUSB0"
BAUD_RATES = 9600    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠
print('hi')
try:
    while X:
        if ser.in_waiting:    # 若收到序列資料…
            message="進來坐坐"
            print('go')          
            data_raw = ser.read(10) # 讀取一行
            data_raw=data_raw.decode()
            real_data=''
            for i in range(9):
                real_data+=data_raw[i]
            idd=real_data
            timetime=time.ctime()
            timetime=str(timetime)
            idd=str(idd)

            print(type(idd))
            print(type(timetime))
            print(idd)
            print(timetime)
            verify=uptodatabase.verify(idd)
            verifyy=uptodatabase.verifyy(idd)
            if(verify):
                if(verifyy):
                    speech_text="請問你為何而來"
                    output=gTTS(text=speech_text, lang='zh-tw', slow=False)
                    output.save('Why.mp3')
                    os.system('mpg321 Why.mp3')
                    message=mictest.Speech()
                    uptodatabase.pushup(idd,timetime,message)
                else:
                    speech_text="你上次沒刷出"
                    output=gTTS(text=speech_text, lang='zh-tw', slow=False)
                    output.save('accessinfail.mp3')
                    os.system('mpg321 accessinfail.mp3')
            else:
                speech_text="請先註冊喔咩噗"
                output=gTTS(text=speech_text, lang='zh-tw', slow=False)
                output.save('fail.mp3')
                os.system('mpg321 fail.mp3')
            time.sleep(1)
except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    print('再見！')

# uptodatabase.pushup("B08901049","2020-12-18")
