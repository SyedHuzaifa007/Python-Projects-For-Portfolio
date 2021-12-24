from email import message
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

chat_list = []
with open(Text_file, mode = 'r', encoding = 'utf8') as f:
    data = f.readlines()
final_data_set = data[1:]
for line in final_data_set:
    data = line.split("-")[0]
    tim = line.split(",")[0].split(",")[1]
    name = line.split(":")[1].split('-')[1]
    message = line.split(":")[2][:-1]
    chat_list.append([data, tim, name, message])
df = pd.DataFrame(chat_list, 
columns = ['Date', 'Time', 'Name', 'Message'])
df.to_excel("Chat_Backup.xlsx", index = False)
