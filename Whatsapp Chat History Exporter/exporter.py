from typing import Text
import urllib.request
import pandas as pd
from pushbullet import PushBullet

Access_token = 'Your Access Token Here'
pb = PushBullet(Access_token)
all_pushes = pb.get_pushes()
latest_one = all_pushes[0]
url = latest_one['file.url']
Text_file = "All_Chats.txt"
urllib.request.urlretrieve(url, Text_file)
