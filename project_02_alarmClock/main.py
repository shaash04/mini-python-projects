import time 
import datetime
import winsound
alarm_time=input("enter the time you want to set alarm for(HH:MM:SS)")
while True:
    current_time=datetime.datetime.datetime.now().strftime("%H:%M:%S")
    print("Current time:", current_time, end="\r") 
    if current_time==alarm_time:
        print("alarm ringing wake up")
        for i in range(2):
            winsound.Beep(2500, 5000)  # frequency=2500Hz, duration=1000ms (1 sec)
        break
    time.sleep(5)