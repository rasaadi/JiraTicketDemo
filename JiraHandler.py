from jira import JIRA
import requests
import JiraException

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class JiraHandler:
    __jiraOptions = {
        'server': 'http://localhost:8080/secure/Dashboard.jspa',
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






if __name__ == '__main__':
    myJira = JiraHandler(username='rafsan.saadi@gmail.com', password='Goponio!234jira')



