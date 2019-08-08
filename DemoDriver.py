from JiraHandler import JiraHandler


class DemoDriver:
    myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
    print(myJira.get_projects())

    issue_dict = {
        'project': {'key': "CCI"},
        'summary': "New issue created through JIRA client-9",
        'description': "This is the description for the new JIRA issue",
        'issuetype': {'name': "Bug"}
    }
    # myJira.create_new_issue(fields=issue_dict)
    # myJira.create_new_issue(project={'key': "CCI"}, summary="New issue created through JIRA client-11",
    #                         description="This is the description for the new JIRA issue-11", issuetype={'name': "Bug"})

    print(myJira.get_issue_by_id('CCI-15'))
    # print(myJira.get_all_issues_for_project('CCI'))
    # myJira.get_all_issues_for_project('CCI')
    myJira.get_all_issues_assigned_to_current_user()

