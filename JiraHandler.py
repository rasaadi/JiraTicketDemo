from jira import JIRA
import requests
import JiraException

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class JiraHandler:
    jira_options = {
        'server': 'http://localhost:8080',
        'verify': False
    }

    jira_client = None

    def __init__(self, **kwargs):
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
                self.jira_client = JIRA(self.jira_options, basic_auth=(self.username, self.password))
            except:
                raise JiraException("Failed to create JIRA client. Please provide valid User credentials ")



    def get_projects(self, raw=False):
        project_list = []
        for project in self.jira_client.projects():
            if raw:
                project_list.append(project)
            else:
                project_list.append({'KEY': project.key, 'NAME': project.name, 'ID': project.id})
        return project_list

    def create_new_issue(self, **kwargs):
        if len(kwargs) != 7:
            raise JiraException("Provide details to create new issue")

        try:
            new_issue = self.jira_client.create_issues(project=kwargs['project'], summary=kwargs['summary'],
                                                       description=kwargs['description'],
                                                       components={'id': kwargs['components']},
                                                       assignee={'name': kwargs['assignee']},
                                                       issuetype={'name': kwargs['description']})
        except:
            raise JiraException("Not enough details was specified to create the issue")



    def crate_new_issue_2(self, **kwargs):
        try:
            new_issue = self.jira_client(project=kwargs['project'], summary=kwargs['summary'],
                                         description=kwargs['description'], issuetype={'name': kwargs['Bug']})
        except:
            raise JiraException("Not enough details was specified to create the issue")
        #
        # new_issue = JIRA.create_issues(project='CCI', summary='New issue created through JIRA client',
        #                                description='This is the description for the new JIRA issue',
        #                                issuetype={'name': 'Bug'})
        # new_issue = JIRA.create_issue(project='CCI', summary='New issue from jira-python',
        #                   description='Look into this one', issuetype={'name': 'Bug'})


    issue_dict = {
        'project': {'id': 10000},
        'summary': 'New issue from jira-python',
        'description': 'Look into this one',
        'issuetype': {'name': 'Bug'},
    }

    def crate_new_issue_3(self, fields=issue_dict):
        new_issue = self.jira_client(fields)




    # def get_issue_by_id(self, issueID):
    #     issue = JIRA.issue(issueID)
    #     return issue

        "https://github.com/r3ap3rpy/python/blob/master/JiraAPIWrapper.py"
        "https://www.youtube.com/watch?v=Nh01NDSRG1s"
        "https://jira.readthedocs.io/en/latest/examples.html#quickstart"


if __name__ == '__main__':
    myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
    print(myJira.get_projects())
    myJira.crate_new_issue_3()
