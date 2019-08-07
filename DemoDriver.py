from JiraHandler import JiraHandler


class DemoDriver:
    myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
    print(myJira.get_projects())
    # print(myJira.get_issue_by_id('CCI-2'))
    # myJira.crate_new_issue_2(project='CCI', summary='New issue created through JIRA client',
    #                           description='This is the description for the new JIRA issue',
    #                           issuetype={'name': 'Bug'})

    issue_dict = {
        'project': {'id': 10000},
        'summary': 'New issue from jira-python',
        'description': 'Look into this one',
        'issuetype': {'name': 'Bug'},
    }

    myJira.crate_new_issue_3(issue_dict)
