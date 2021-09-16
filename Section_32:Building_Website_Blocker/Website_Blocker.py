import time
#check for the time of day
from datetime import datetime as dt

hosts_path = 'etc/hosts'
redirect = '127.0.0.1'
website_list = 'www.facebook.com', 'facebook.com', 'www.reddit.com', 'reddit.com'

while True:
    #instead of putting current year, python will generate the year for sustainability
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        print("Working hours")
    else:
        print("Fun hours")
    time.sleep(3)