import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)

url = github_api + '/repos/cloudops7/project1/pulls?state=all'
commits = gh_session.get(url = url)
commits_json = commits.json()
for dict_item in commits_json:
    print(f"PR Message: {dict_item['title']} \nState : {dict_item['state']}")
    print(f"User details:\n   Login:{dict_item['user']['login']} \n   ID: {dict_item['user']['id']}")