# website_blocker-python_script
will edit hosts file to block certain websites during set hours in the day


TO INSTALL:

clone repo to computer, somewhere it wont get touched.

Then we will use crontab to make it a system process.

From Terminal, write:  


crontab -e



this brings up the crontab editor in vim

type in:


15 * * * * /Users/YourUsername/website_blocker/website_blocker-python_script/blocker_script.py
  
(the numbers/* in front specify when the script will run and are: minutes, hours, day, month, day of week, respectively)


type:

^C 
:wq (Enter)


This saves the crontab file and exits vim.

type:

crontab -l   Your new script should show up.

RESTART Computer for changes to take effect.

Any suggestions or improvements please reach out or throw me a pull request!

