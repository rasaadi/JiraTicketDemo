import time

from JiraHandler import JiraHandler
from OpenWeather import OpenWeather


class DemoDriver:
    myWeather = OpenWeather()
    target_city = "Mountain View"

    if isinstance(target_city, str):
        weather_api_url = myWeather.url_constructor(target_city, None)
    else:
        weather_api_url = myWeather.url_constructor(None, target_city)

    # weather_api_url = myWeather.url_constructor(target_city)
    weather_json = myWeather.make_weather_api_request(weather_api_url)
    current_temp = myWeather.get_current_temperature(weather_json)
    print("{} temperature is {}".format(target_city, current_temp))

    # project = {'key': "CCI"}
    # summary = "ATTENTION: {}'s temperature is changed to {}".format(target_city, current_temp)
    # print(summary)
    # description = "Temperature for {} has changed to {}. It requires urgent attention.".format(target_city, current_temp)
    # print(description)
    # issuetype = {'name': "Bug"}

    issue_dict = {
        'project': {'key': "CCI"},
        'summary': "[ATTENTION] {} current temperature is changed to {}F".format(target_city, current_temp),
        'description': "Temperature for {} has changed to {}F. It requires urgent attention.".format(target_city,
                                                                                                     current_temp),
        'issuetype': {'name': "Bug"}
    }

    if current_temp < 65.46 or current_temp > 80:
        myJira = JiraHandler(username='rafsan.saadi', password='Pass!23')
        # myJira.create_new_issue(project=project, summary=summary, description=description, issuetype=issuetype)
        myJira.create_new_issue(fields=issue_dict)





########################################TEST CODE#############################################################
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
