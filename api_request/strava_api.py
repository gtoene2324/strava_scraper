import pandas as pd
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize the dataframe
col_names = ['id','type']
activities = pd.DataFrame(columns=col_names)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

# TODO - import these from a json file, that's stored in secrets. similar to my py-fin stuff
payload = {
    'client_id': "69903",
    'client_secret': '84def7ca74a1e39fc6c1fae5be0a96a69ca0bcdc',
    'refresh_token': 'e32e4b397a53d9e2f0ef4f221d664efb0530b48e',
    'grant_type': "refresh_token",
    'f': 'json'
}
print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

# still getting an auth error
print(my_dataset)