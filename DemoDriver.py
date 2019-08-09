from JiraHandler import JiraHandler
from OpenWeather import OpenWeather


class DemoDriver:
    # myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
    # print(myJira.get_projects())
    #
    # issue_dict = {
    #     'project': {'key': "CCI"},
    #     'summary': "New issue created through JIRA client-9",
    #     'description': "This is the description for the new JIRA issue",
    #     'issuetype': {'name': "Bug"}
    # }
    # # myJira.create_new_issue(fields=issue_dict)
    # # myJira.create_new_issue(project={'key': "CCI"}, summary="New issue created through JIRA client-11",
    # #                         description="This is the description for the new JIRA issue-11", issuetype={'name': "Bug"})
    # #
    # print(myJira.get_issue_by_id('CCI-15'))
    # myJira.get_all_issues_for_project('CCI')
    # myJira.get_all_issues_assigned_to_current_user()

    # myJira.update_issue_details('CCI-15', summary='this is the new updated summery for CCI-15')

    myWeather = OpenWeather()
    city = 94040

    URL = myWeather.url_constructor(city)
    weatherJson = myWeather.get_weather(URL)
    temperature = myWeather.get_current_temperature(weatherJson)
    print(temperature)

    project = {'key': "CCI"}
    summary = "ATTENTION: {}'s temperature is changed to {}".format(city, temperature)
    print(summary)
    description = "Temperature for {} has changed to {}. It requires urgent attention.".format(city, temperature)
    print(description)
    issuetype = {'name': "Bug"}

    if temperature < 65.46 or temperature > 80:
        myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
        myJira.create_new_issue(project=project, summary=summary, description=description, issuetype=issuetype)




