from jira import JIRA
import requests
import JiraException

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class JiraHandler:
    JIRA_OPTIONS = {
        'server': 'http://localhost:8080',
        'verify': False
    }

    JIRA_CLIENT = None

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

    def choose_field_type(self, fields=None, **fieldargs):
        if fields is not None:
            return {'fielfs': fields}
        return {'fields': fieldargs}

    def crate_new_issue(self, fields=None):
        if fields is not None:
            try:
                new_issue = self.JIRA_CLIENT.create_issue(fields)
                print("Jira issue created: {}".format(new_issue))
            except:
                raise JiraException("Not enough details was specified to create the issue")
            return new_issue
        else:
            raise JiraException("Did not specify ISSUE details")

    def create_new_issue(self, **fieldargs):
        if len(fieldargs) != 4:
            raise JiraException("Provide details to create new issue")

        try:
            new_issue = self.JIRA_CLIENT.create_issue(project=fieldargs['project'], summary=fieldargs['summary'],
                                                      description=fieldargs['description'],
                                                      issuetype=fieldargs['issuetype'])
            return new_issue
            print("Jira issue created: {}".format(new_issue))
        except:
            raise JiraException("Not enough details was specified to create the issue")


        # def get_issue_by_id(self, issueID):
        #     issue = JIRA.issue(issueID)
        #     return issue

        "https://github.com/r3ap3rpy/python/blob/master/JiraAPIWrapper.py"
        "https://www.youtube.com/watch?v=Nh01NDSRG1s"
        "https://jira.readthedocs.io/en/latest/examples.html#quickstart"


if __name__ == '__main__':
    myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
    print(myJira.get_projects())
    issue_dict = {
        'project': {'key': "CCI"},
        'summary': "New issue created through JIRA client-5",
        'description': "This is the description for the new JIRA issue",
        'issuetype': {'name': "Bug"}
    }
    myJira.crate_new_issue(fields=issue_dict)
    myJira.create_new_issue(project={'key': "CCI"}, summary="New issue created through JIRA client-6",
                            description="This is the description for the new JIRA issue", issuetype={'name': "Bug"})
