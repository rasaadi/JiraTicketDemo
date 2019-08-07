from JiraHandler import JiraHandler


class DemoDriver:
    myJira = JiraHandler(username='rafsan.saadi', password='Goponio!234jira')
    print(myJira.get_projects())
