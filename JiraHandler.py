'''
Reference URL: https://jira.readthedocs.io/en/latest/index.html
'''

from jira import JIRA
import requests
import JiraException


class JiraHandler:
    JIRA_OPTIONS = {
        'server': 'http://localhost:8080',
        'verify': False
    }

    JIRA_CLIENT = None

    def __init__(self, **kwargs):
        print("[RS] Instantiate JiraHandler Object")
        if len(kwargs) != 2:
            raise JiraException("Must provide Username and password as arguments")
        else:
            if 'username' in kwargs.keys():
                self.username = kwargs['username']
            else:
                raise JiraException("Missing username")

            if 'password' in kwargs.keys():
                self.password = kwargs['password']
            else:
                raise JiraException("Missing password")

            # Creating JIRA client
            try:
                self.JIRA_CLIENT = JIRA(self.JIRA_OPTIONS, basic_auth=(self.username, self.password))
            except:
                raise JiraException("Failed to create JIRA client. Please provide valid User credentials ")

    def get_projects(self, raw=False):
        project_list = []
        for project in self.JIRA_CLIENT.projects():
            if raw:
                project_list.append(project)
            else:
                project_list.append({'KEY': project.key, 'NAME': project.name, 'ID': project.id})
        return project_list

    def crate_new_issue_with_fields(self, fields=None):
        if fields is not None:
            try:
                new_issue = self.JIRA_CLIENT.create_issue(fields)
                print("Jira issue created: {}".format(new_issue))
            except:
                raise JiraException("Not enough details was specified to create the issue")
            return new_issue
        else:
            raise JiraException("Did not specify ISSUE details")

    def create_new_issue_with_fieldargs(self, **fieldargs):
        if len(fieldargs) != 4:
            raise JiraException("Provide details to create new issue")

        try:
            new_issue = self.JIRA_CLIENT.create_issue(project=fieldargs['project'], summary=fieldargs['summary'],
                                                      description=fieldargs['description'],
                                                      issuetype=fieldargs['issuetype'])
            print("Jira issue created: {}".format(new_issue))
        except:
            raise JiraException("Not enough details was specified to create the issue")
        return new_issue

    def create_new_issue(self, fields=None, **fieldargs):
        print("[RS] Creating new JIRA issue")
        if fields is not None and len(fieldargs) == 0:
            self.crate_new_issue_with_fields(fields)
        elif len(fieldargs) == 4 and fields == None:
            self.create_new_issue_with_fieldargs(**fieldargs)
        else:
            raise JiraException("Cannot create jira ISSUE with provided info")

    def get_issue_by_id(self, issueID):
        issue_details = []
        try:
            issue = self.JIRA_CLIENT.issue(issueID)
        except:
            raise JiraException("Failed to find the target ISSUE")

        issue_details.append(
            {'PROJECT': issue.fields.project, 'SUMMARY': issue.fields.summary, 'DESCRIPTION': issue.fields.description,
             'STATUS': issue.fields.status})

        return issue_details

    def get_all_issues_for_project(self, projects=None):
        if projects is not None:
            project_name = 'project={}'.format(projects)

        try:
            issues_in_project = self.JIRA_CLIENT.search_issues(project_name)
        except:
            raise JiraException("No issue found for the project")

        for issue in issues_in_project:
            print('{}: {}'.format(issue.key, issue.fields.summary))

    def get_all_issues_assigned_to_current_user(self):
        try:
            all_my_issues = self.JIRA_CLIENT.search_issues(
                'assignee = currentUser() AND status in (Open, "In Progress")')
        except:
            raise JiraException("No issue found for the current user")
        for issue in all_my_issues:
            print('{}: {}'.format(issue.key, issue.fields.summary))


    # def update_issue_details(self, **detailargs):
    #     if len(detailargs) < 3:
    #         raise JiraException("Minimum 2 agruments need to be specified")
    #
    #     target_issue = self.JIRA_CLIENT.issue(issueID)
        # target_issue.update(fields={'summary': 'new summary', 'description': 'A new summary was added'})
        # target_issue.update(summary=detailargs['summary'], description= detailargs['description'])

        # new_issue = self.JIRA_CLIENT.create_issue(project=fieldargs['project'], summary=fieldargs['summary'],
        #                                           description=fieldargs['description'],
        #                                           issuetype=fieldargs['issuetype'])



########################################TEST CODE#############################################################
# if __name__ == '__main__':
#     myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
#     print(myJira.get_projects())
#     issue_dict = {
#         'project': {'key': "CCI"},
#         'summary': "New issue created through JIRA client-5",
#         'description': "This is the description for the new JIRA issue",
#         'issuetype': {'name': "Bug"}
#     }
#     myJira.crate_new_issue_with_fields(fields=issue_dict)
#     myJira.create_new_issue_with_fieldargs(project={'key': "CCI"}, summary="New issue created through JIRA client-6",
#                                            description="This is the description for the new JIRA issue", issuetype={'name': "Bug"})
