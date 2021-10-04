# Importing Modules
import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
website = input("Enter The Name of The Website You Want To Block: ")
web_url = "www." + website + ".com"
websites_list = [web_url]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)