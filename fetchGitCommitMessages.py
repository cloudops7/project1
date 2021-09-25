import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)

url = github_api + '/repos/cloudops7/project1/commits'
commits = gh_session.get(url = url)
commits_json = commits.json()
for dict_item in commits_json:
    print(dict_item['commit']['message'])