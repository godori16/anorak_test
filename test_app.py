import requests
import time
import json
import matplotlib.pyplot as plt

class telemetry_controller:
  def __init__(self, server, JWT_token):
    self.server = server
    self.headers = {"Accept": "*/*",
    "Content-Type": "application/json",
    "X-Authorization": JWT_token}

  def getTimeseries(self, entityType, entityId, keys, startTs, endTs, limit=100):
    url = f'{self.server}/api/plugins/telemetry/{entityType}/{entityId}/values/timeseries?limit={limit}&agg=NONE&keys={keys}&startTs={startTs}&endTs={endTs}'
    return requests.get(url, headers=self.headers)

anorak_server = "http://182.218.64.133:8080"
anorak_JWT_token ="Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI4OTcyZTI5MC03OWU5LTExZWEtYmNkZi0yMTQzNzllMmY1M2EiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiODhkNGE2YzAtNzllOS0xMWVhLWJjZGYtMjE0Mzc5ZTJmNTNhIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNTg3NzMwMzA3LCJleHAiOjE1ODc3MzkzMDd9.QCWepS71hpJ1w0ANwyJqVzRix_TASyUV4UeCrmVyOF2Z4AAnsPfU5sqApGrYGJVtg6nHVKtYsyj5PmoJRke9fg"
anorak_telemetry_controller = telemetry_controller(anorak_server, anorak_JWT_token)

entityType = 'DEVICE'
entityId = 'a5bc42d0-79ed-11ea-b017-73cde00557cc'
keys = 'RMS_a'
startTs = 0
endTs = int(time.time()*1000)
response = anorak_telemetry_controller.getTimeseries(entityType, entityId, keys, startTs, endTs, limit=1000)

print(response.status_code)
print(response.text)

response_dict = json.loads(response.text)

time = [ int(item['ts']) for item in response_dict['RMS_a'] ]
value = [ float(item['value']) for item in response_dict['RMS_a'] ]

plt.figure()
plt.plot(time, value)

