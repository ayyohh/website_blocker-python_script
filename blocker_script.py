import time
from datetime import datetime as dt

hosts_path='/etc/hosts'
redirect='127.0.0.1'
# EDIT THE WEBSITE LIST TO SUIT YOUR NEEDS
website_list=['www.facebook.com', 'facebook.com']

while True:
    # if time between 8am and 6pm, website blocker commences
    # EDIT TIME TO YOUR NEEDS
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print('Work hard...')

        # opens hosts file and prints contents
        with open(hosts_path, 'r+') as file:
            content=file.read()
            print(content)
            # checks to see if website is in hosts file, yes? pass, no? write to file
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')


    else:
        # outside our work hours, the website should become avaiable again
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            # after the hosts file opens, we iterate through every line
            # every line that doesn't have a website in it will be rewritten over the current file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print(content)
        print('Play harder...')
    time.sleep(15)
