# Importing Required Moduels
from contextlib import closing
import time
from time import clock_gettime_ns, sleep
from sinchsms import SinchSMS

# Defining Fucntion For Sending SMS
def send_sms():
    number = ''
    app_key = ''
    app_secret = ''

    message = ''

    client = SinchSMS(app_key, app_secret)
    print("Sending '%s' to '%s'" % (message, number))

    