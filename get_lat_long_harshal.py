import requests
import base64
import json

api_url = 'https://my.geotab.com/apiv1'
username = 'geotab.api@intersection.com'
password = '$Zw1=Eq6&o4#'
database = 'intersection'
# search = {'serialNumber': 'G9Y59K6R61W0'}
# results_options = {'resultsLimit': 1, 'fromDate': '2023-02-22T00:00:00.000Z'}
# params = {'search': search,
#           'resultsOptions': results_options}

payload = {
    "method": "Get",
    "params": {
        "typeName": "LogRecord",
        "search": {
            "fromDate": "2023-03-02",
            "serialNumber": "G9Y59K6R61W0"
        },
        "resultsLimit": 1,
        "credentials": {
            "database": database,
            "userName": username,
            "password": password
        }
    }
}

headers = {'Authorization': 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()}
response = requests.post(api_url, headers=headers, data=json.dumps(payload))
data = response.json()
if data['result']:
    lat, lon = data['result'][0]['latitude'], data['result'][0]['longitude']
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("No data found")

