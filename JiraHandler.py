from jira import JIRA
import requests
import JiraException

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class JiraHandler:
    __jiraOptions = {
        'server': 'http://localhost:8080',
        'verify': False
    }

    __jiraClient = None

    def __init__(self, **kwargs):
        if len(kwargs) != 2:
            raise JiraException("Must provide Username and password as arguments")
        else:
            if 'username' in kwargs.keys():
                self.__username = kwargs['username']
            else:
                raise JiraException("Must provide username")

            if 'password' in kwargs.keys():
                self.__password = kwargs['password']
            else:
                raise JiraException("Must provide password")

            try:
                self.__jiraClient = JIRA(self.__jiraOptions, basic_auth=(self.__username, self.__password))
            except:
                raise JiraException("Failed to create JIRA client to connect Jira API")




    def get_projects(self, raw = False):
        project_list = []
        for project in self.__jiraClient.projects():
            if raw:
                project_list.append(project)
            else:
                project_list.append({'KEY': project.key, 'NAME': project.name})
        return project_list

    def create_new_issue(self, issue, comment):
        "https://github.com/r3ap3rpy/python/blob/master/JiraAPIWrapper.py"
        "https://www.youtube.com/watch?v=Nh01NDSRG1s"
        "https://jira.readthedocs.io/en/latest/examples.html#quickstart"




#
# if __name__ == '__main__':
#     myJira = JiraHandler(username='rafsan.saadi', password='Goponio!234jira')



