# JiraTicketDemo
Jira Ticket Demo for `Senior Software/Security Engineer`

### Problem:
Security Vulnerabilities are event driven should be persisted in JIRA. Rest API integration and maintaining data quality 
and integrity is a key component of the Development Security Platform. 

### Demo requirements:
Create `functional` POC/wireframe using AWS Lambda/Python serverless application that can be used to `create JIRAs` once 
a certain monitored condition is met (e.g. Temperature obtained from weather underground `RestAPI`).
Suggest/implement additional features that could be considered.
Present and outline the solution key points, customer benefits, and security considerations.

### Notes: 
Use the free JIRA test instance or local JIRA development.

========================================================================================================================
### Sample Open Weather API output:
```json
// https://api.openweathermap.org/data/2.5/weather?zip=95051&APPID=349573272b4f8cf9a6c3ce64750b5d83&units=imperial

{
  "coord": {
    "lon": -121.98,
    "lat": 37.35
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 73.36,
    "pressure": 1016,
    "humidity": 53,
    "temp_min": 68,
    "temp_max": 78.01
  },
  "visibility": 16093,
  "wind": {
    "speed": 8.05,
    "deg": 30
  },
  "clouds": {
    "all": 20
  },
  "dt": 1565294433,
  "sys": {
    "type": 1,
    "id": 5845,
    "message": 0.0105,
    "country": "US",
    "sunrise": 1565270289,
    "sunset": 1565320143
  },
  "timezone": -25200,
  "id": 0,
  "name": "Santa Clara",
  "cod": 200
}
```

### Sample JIRA ticket:
![Alt text](https://github.com/rasaadi/JiraTicketDemo/blob/master/SampleJiraTicket.png?raw=true "SampleJiraTicket")

