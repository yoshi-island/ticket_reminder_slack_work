#coding: utf-8
# python3.5.0

# ======================
# ssl error avoidance
import urllib3
urllib3.disable_warnings()

# ======================
## import modules
from jira_ticket_reminder_to_slack_vars import *

# ======================
## get jira tickets and post slack

def GetJiraIssues(url, params):

    # JIRA
    options = {
    'server': jira_server,
    'verify': False,
    'rest_api_version': '2',
    }

    jira = JIRA(options, basic_auth=(username, jira_password))

    # get issues
    all_proj_issues = jira.search_issues(jira_filter)
    list_summary = [issues_in_proj.fields.summary for issues_in_proj in all_proj_issues]
    list_key = [issues_in_proj.key for issues_in_proj in all_proj_issues]
    #list_status = [issues_in_proj.fields.status.name for issues_in_proj in all_proj_issues]
    list_assignee = [issues_in_proj.fields.assignee.key for issues_in_proj in all_proj_issues]
    list_due = [issues_in_proj.fields.customfield_10857 for issues_in_proj in all_proj_issues]

    # text message
    params['text'] = '%s %s' % (today,greetings)

    #quit when no tickets listed
    if len(list_summary) == 0:

        params['text'] = 'All tickets are gone! :tada:'
        req = urllib.request.Request(url) #python3
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        params = urllib.parse.urlencode(params).encode('utf-8') #python3

        with urllib.request.urlopen(req, params) as res: #python3
            data = res.read().decode("utf-8")
            print(data)
            sys.exit()

    # send tickets info as an attachments
    c = int(0)
    for i in list_summary:
      send_line = list_assignee[c] + " " +  list_due[c] + "\r\n"
      print(params['attachments'])
      params['attachments'][c]['title'] = list_summary[c]
      params['attachments'][c]['title_link'] = jira_server + '/browse/' + list_key[c]
      params['attachments'][c]['text'] = send_line
      params['attachments'][c]['color'] = "#7CD197" # color green

      c += 1
      params['attachments'].append({'color': '#7CD197'})


    # send to slack
    req = urllib.request.Request(url) #python3
    req.add_header('Content-Type', 'application/x-www-form-urlencoded') #header
    params = urllib.parse.urlencode(params).encode('utf-8') #python3

    with urllib.request.urlopen(req, params) as res: #python3
        data = res.read().decode("utf-8")
        print(data)

# ======================
# execution

if __name__ == "__main__":
    GetJiraIssues(url, params)

