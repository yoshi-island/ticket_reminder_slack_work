#coding: utf-8
# python3.5.0

# ======================
## import modules

import sys
import getpass
from jira.client import JIRA
# http://jira.readthedocs.io/en/master/index.html
import urllib.request, urllib.error 
import datetime #pip install python-dateutil
import calendar
from dateutil.relativedelta import relativedelta

# ======================
## personal info(mandatory)

# import personal info from other file
from password_list import *

#username = 'hogehoge'
#jira_password = getpass.getpass("Enter Your JIRA Password Here: ")
#jira_password = 'hogehoge'

#slack_token = 'hogehoge'
#post_channel = 'hogehoge'

#jira_filter = 'type = Sub-task'
#jira_server = 'http://hogehoge.com'

#greetings = 'hello!'

#slack_user = 'hogehoge'

# ======================
## set variables(optional)

#slack_botname = 'hogehoge'
#slack_icon = ':information_desk_person::skin-tone-3:'

# ======================
## set date
today = datetime.date.today()

# ======================
## set slack info

url = "https://slack.com/api/chat.postMessage"
params = {'token': slack_token,
        'channel': post_channel,
        #'text': 'error', # default text
        #'icon_emoji': slack_icon,
        "attachments": [
        {
        #    "fallback": "error",
        #    "pretext": "error",
        #    "title": "error",
        #    "title_link": "https://google.com",
        #    "text": "error",
            "color": "#7CD197"
        }],
        'as_user': slack_user
        #'username': slack_botname
        }

# ======================
