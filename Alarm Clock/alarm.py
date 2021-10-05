# Imported Libraries & Modules
import datetime
import time
from tkinter import *
import winsound

# Creating An Infinite Loop
def alarm():
    while True:
        # Set Alarm Time
        set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait For One Seconds
        time.sleep(1)