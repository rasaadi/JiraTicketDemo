from jira import JIRA
import requests
import JiraException



# jiraC = JIRA('http://localhost:808')
auth_jiraC= JIRA('http://localhost:808', basic_auth=('rafsan.saadi', 'Pass!23'))





# class JiraTrail:
#     jiraOptions = {
#         'server': 'http://localhost:8080',
#         'verify': False
#     }
#
#     jiraClient, username, password = None
#
#     def __init__(self, username, password):
#         try:
#             self.jiraClient = JIRA(self.jiraOptions, basic_auth=(username, password))
#         except:
#             raise JiraException("Failed to create JIRA client. Please provide valid User credentials ")
#
#     def get_projects(self, raw=False):
#         project_list = []
#         for project in self.jiraClient.projects():
#             if raw:
#                 project_list.append(project)
#             else:
#                 project_list.append({'KEY': project.key, 'NAME': project.name, 'ID': project.id})
#         return project_list
#
#
#
#
# if __name__ == '__main__':
#
#     myJira = JiraTrail('rafsan.saadi', 'Pass!23')
#
#     myJira. get_projects()